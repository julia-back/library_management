from rest_framework.serializers import ModelSerializer
from .models import ReceiptBook


class ReceiptBookSerializer(ModelSerializer):
    class Meta:
        model = ReceiptBook
        fields = "__all__"
