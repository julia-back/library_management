from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, AuthorRetrieveSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache


class BookCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания книги, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class BookListAPIView(generics.ListAPIView):
    """
    Представление для предоставления списка книг, доступно только всем
    авторизованным пользователям.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ["name", "description", "genre"]
    ordering_field = ["name", "author"]
    filterset_fields = ["serial_number", "language", "author", "genre", "publishing_house"]

    def get_queryset(self):
        queryset = cache.get("book_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("book_queryset_all", queryset, 60 * 5)
        return queryset


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для предоставления деталей книги, доступно всем
    авторизованным пользователям.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = cache.get("book_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("book_queryset_all", queryset, 60 * 5)
        return queryset


class BookUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления книги, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class BookDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления книги, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class AuthorCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания автора, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer


class AuthorListAPIView(generics.ListAPIView):
    """
    Представление для предоставления списка авторов, доступно всем
    авторизованным пользователям.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = cache.get("author_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("author_queryset_all", queryset, 60 * 5)
        return queryset


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для предоставления деталей автора, доступно всем
    авторизованным пользователям.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorRetrieveSerializer

    def get_queryset(self):
        queryset = cache.get("author_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("author_queryset_all", queryset, 60 * 5)
        return queryset


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления автора, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления автора, доступно только пользователям,
    состоящим в группе администраторов.
    """

    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer
