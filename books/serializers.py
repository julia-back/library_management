from rest_framework.serializers import ModelSerializer
from .models import Book, Author


class BookSerializer(ModelSerializer):
    """Класс сериализатора для модели книги."""

    class Meta:
        model = Book
        fields = ["id", "serial_number", "name", "description", "author", "genre",
                  "language", "publishing_house", "place_of_publication",
                  "publication_year", "receipt_status"]
        extra_kwargs = {
            "id": {"read_only": True}
        }


class AuthorSerializer(ModelSerializer):
    """Класс сериализатора для модели автора."""

    class Meta:
        model = Author
        fields = "__all__"
