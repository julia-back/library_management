from rest_framework import generics
from .models import ReceiptBook
from .serializers import ReceiptBookSerializer
from datetime import date


class CreateReceiptBookAPIView(generics.CreateAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        book = serializer.book
        book.receipt_status = "on_hands"
        book.save()


class DestroyReceiptBookAPIView(generics.DestroyAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []


class ReturnBookAPIView(generics.GenericAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.return_date = date.today()
        serializer = self.get_serializer(instance)
        serializer.save()
        book = instance.book
        book.receipt_status = "free"
        book.save()


class ListReceiptBookAPIView(generics.ListAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class RetrieveReceiptBookAPIView(generics.RetrieveAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []
