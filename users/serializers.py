from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    """Класс сериализатора для модели пользователя."""

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]


class UserCreateSerializer(ModelSerializer):
    """Класс сериализатора для создания модели пользователя."""

    class Meta:
        model = User
        fields = ["email", "username", "password"]
