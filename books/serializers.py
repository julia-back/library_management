from rest_framework.serializers import ModelSerializer
from .models import Book, Author


class BookSerializer(ModelSerializer):
    """Класс сериализатора для модели книги."""

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    """Класс сериализатора для модели автора."""

    class Meta:
        model = Author
        fields = "__all__"
