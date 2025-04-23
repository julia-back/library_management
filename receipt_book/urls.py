from django.urls import path
from .apps import ReceiptBookConfig
from . import views


app_name = ReceiptBookConfig.name

urlpatterns = [
    path("receipt_create/", views.CreateReceiptBookAPIView.as_view(), name="receipt_create"),
    path("receipt_destroy/", views.DestroyReceiptBookAPIView.as_view(), name="receipt_destroy"),
    path("receipt_list/", views.ListReceiptBookAPIView.as_view(), name="receipt_list"),
    path("receipt_retrieve/", views.RetrieveReceiptBookAPIView.as_view(), name="receipt_retrieve"),
]
