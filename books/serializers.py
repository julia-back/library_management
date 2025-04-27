from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели книги."""

    class Meta:
        model = Book
        fields = ["id", "serial_number", "name", "description", "author", "genre",
                  "language", "publishing_house", "place_of_publication",
                  "publication_year", "receipt_status"]
        extra_kwargs = {
            "id": {"read_only": True}
        }


class BookByAuthorSerializer(serializers.ModelSerializer):
    """Класс сериализатора модели книги для использования в поле books в сериализаторе деталей автора."""

    class Meta:
        model = Book
        fields = ["name", "description", "genre", "language"]


class AuthorSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели автора."""

    class Meta:
        model = Author
        fields = "__all__"


class AuthorRetrieveSerializer(serializers.ModelSerializer):
    """Класс сериализатора для модели конкретного автора."""

    books = BookByAuthorSerializer(many=True, source="book_set")

    class Meta:
        model = Author
        fields = "__all__"
