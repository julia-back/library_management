from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    permission_classes = []
    serializer_class = BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = []
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    permission_classes = []
    serializer_class = BookSerializer


class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    permission_classes = []
    serializer_class = BookSerializer


class BookDestroyAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = []
    serializer_class = BookSerializer


class AuthorCreateAPIView(generics.CreateAPIView):
    queryset = Author.objects.all()
    permission_classes = []
    serializer_class = AuthorSerializer


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    permission_classes = []
    serializer_class = AuthorSerializer


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    permission_classes = []
    serializer_class = AuthorSerializer


class AuthorUpdateAPIView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    permission_classes = []
    serializer_class = AuthorSerializer


class AuthorDestroyAPIView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    permission_classes = []
    serializer_class = AuthorSerializer
