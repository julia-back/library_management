from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_field = ["name", "description", "genre"]
    ordering_field = ["name", "author"]
    filterset_fields = ["serial_number", "language", "author", "genre", "publishing_house"]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = BookSerializer


class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AuthorSerializer
