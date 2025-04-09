from django.urls import path
from .apps import BooksConfig
from . import views


app_name = BooksConfig.name

urlpatterns = [
    path("book/new/", views.BookCreateAPIView.as_view(), name="book_create"),
    path("book_list/", views.BookListAPIView.as_view(), name="book_list"),
    path("book/<int:pk>/", views.BookRetrieveAPIView.as_view(), name="book_retrieve"),
    path("book/<int:pk>/", views.BookUpdateAPIView.as_view(), name="book_update"),
    path("book/<int:pk>/", views.BookDestroyAPIView.as_view(), name="book_destroy"),

    path("author/new/", views.AuthorCreateAPIView.as_view(), name="author_create"),
    path("author_list/", views.AuthorListAPIView.as_view(), name="author_list"),
    path("author/<int:pk>/", views.AuthorRetrieveAPIView.as_view(), name="author_retrieve"),
    path("author/<int:pk>/", views.AuthorUpdateAPIView.as_view(), name="author_update"),
    path("author/<int:pk>/", views.AuthorDestroyAPIView.as_view(), name="author_destroy"),

]
