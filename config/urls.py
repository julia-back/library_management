from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("library/", include("books.urls", namespace="library")),
    path("users/", include("users.urls", namespace="users")),
    path("receipt/", include("receipt_book.urls", namespace="receipt")),
]
