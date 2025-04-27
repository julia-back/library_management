from rest_framework import generics
from rest_framework.response import Response
from django.db import transaction
from .models import ReceiptBook
from .serializers import ReceiptBookSerializer, CreateReceiptBookSerializer
from datetime import date
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class CreateReceiptBookAPIView(generics.CreateAPIView):
    """
    Представление для создания выдачи книги, доступно только
    пользователям, состоящим в группе администраторов.
    """

    queryset = ReceiptBook.objects.all()
    serializer_class = CreateReceiptBookSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def perform_create(self, serializer):
        """
        Метод создания выдачи книги. Устанавливает статус книги в 'on_hands'.
        """
        with transaction.atomic():
            receipt = serializer.save()
            book = receipt.book
            book.receipt_status = "on_hands"
            book.save()


class DestroyReceiptBookAPIView(generics.DestroyAPIView):
    """
    Представление для удаления выдачи книги, доступно только
    для пользователей, состоящим в группе администраторов.
    """

    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class ReturnBookAPIView(generics.GenericAPIView):
    """
    Представление для возвращения книги, доступно только
    для пользователей, состоящим в группе администраторов.
    """

    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        """
        Метод для возвращения книги. Проставляет дату возвращения книги
        в выдаче книги. Меняет статус книги на 'free'.
        """

        instance = self.get_object()
        if instance.return_date is None:
            instance.return_date = date.today()

        with transaction.atomic():
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            book = instance.book
            book.receipt_status = "free"
            book.save()

        return Response(serializer.data)


class ListReceiptBookAPIView(generics.ListAPIView):
    """
    Представление для предоставления списка выдачи книг. Доступно всем
    авторизованным пользователям. Для обычных пользователей предоставляет
    список их выдач книг. Для пользователей, состоящих в группе
    администраторов, предоставляет список всех выдач книг.
    """

    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer

    def get_queryset(self):
        """
        Метод получения queryset'а. Для обычных пользователей предоставляет
        список их выдач книг. Для пользователей, состоящих в группе
        администраторов, предоставляет список всех выдач книг.
        """

        queryset = super().get_queryset()
        if self.request.user.groups.filter(name="admin").exists():
            return queryset
        return queryset.filter(user=self.request.user)


class RetrieveReceiptBookAPIView(generics.RetrieveAPIView):
    """
    Представление для предоставления деталей выдачи книги. Доступно
    пользователям, состоящим в группе администраторов, и пользователю,
    являющемуся владельцем по полю user.
    """

    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
