from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularSwaggerView,
                                   SpectacularRedocView)
from rest_framework.permissions import AllowAny


urlpatterns = [
    path("admin/", admin.site.urls),

    path("/schema/", SpectacularAPIView.as_view(permission_classes=[AllowAny]), name="schema"),
    path("/docs/swagger-ui/", SpectacularSwaggerView.as_view(permission_classes=[AllowAny]), name="docs_swagger_ui"),
    path("/docs/redoc/", SpectacularRedocView.as_view(permission_classes=[AllowAny]), name="docs_redoc"),

    path("library/", include("books.urls", namespace="library")),
    path("users/", include("users.urls", namespace="users")),
    path("receipt/", include("receipt_book.urls", namespace="receipt")),
]
