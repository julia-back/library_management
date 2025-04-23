from rest_framework import generics
from .models import ReceiptBook
from .serializers import ReceiptBookSerializer


class CreateReceiptBookAPIView(generics.CreateAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []


class DestroyReceiptBookAPIView(generics.DestroyAPIView):
    queryset = ReceiptBook.objects.all()
    serializer_class = ReceiptBookSerializer
    permission_classes = []


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
