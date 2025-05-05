from django.urls import path
from .apps import BooksConfig
from . import views


app_name = BooksConfig.name

urlpatterns = [
    path("book_create/", views.BookCreateAPIView.as_view(), name="book_create"),
    path("book_list/", views.BookListAPIView.as_view(), name="book_list"),
    path("book_retrieve/<int:pk>/", views.BookRetrieveAPIView.as_view(), name="book_retrieve"),
    path("book_update/<int:pk>/", views.BookUpdateAPIView.as_view(), name="book_update"),
    path("book_destroy/<int:pk>/", views.BookDestroyAPIView.as_view(), name="book_destroy"),

    path("author_create/", views.AuthorCreateAPIView.as_view(), name="author_create"),
    path("author_list/", views.AuthorListAPIView.as_view(), name="author_list"),
    path("author_retrieve/<int:pk>/", views.AuthorRetrieveAPIView.as_view(), name="author_retrieve"),
    path("author_update/<int:pk>/", views.AuthorUpdateAPIView.as_view(), name="author_update"),
    path("author_destroy/<int:pk>/", views.AuthorDestroyAPIView.as_view(), name="author_destroy"),
]
