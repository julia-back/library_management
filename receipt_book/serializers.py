from rest_framework import serializers
from .models import ReceiptBook


class ReceiptBookSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели выдачи книги."""

    class Meta:
        model = ReceiptBook
        fields = "__all__"


class CreateReceiptBookSerializer(serializers.ModelSerializer):
    """Класс сериализатора для создания модели выдачи книги."""

    class Meta:
        model = ReceiptBook
        fields = "__all__"

    def validate(self, attrs):
        book = attrs.get("book")
        if book.receipt_status == "on_hands":
            raise serializers.ValidationError("Книга уже на руках.")
        return attrs
