from rest_framework.serializers import ModelSerializer
from .models import ReceiptBook


class ReceiptBookSerializer(ModelSerializer):
    """Класс сериализатора для модели выдачи книги."""

    class Meta:
        model = ReceiptBook
        fields = "__all__"
