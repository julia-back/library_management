from django.urls import path
from .apps import ReceiptBookConfig
from . import views


app_name = ReceiptBookConfig.name

urlpatterns = [
    path("receipt/new/", views.CreateReceiptBookAPIView.as_view(), name="receipt_create"),
    path("receipt_destroy/<int:pk>/", views.DestroyReceiptBookAPIView.as_view(), name="receipt_destroy"),
    path("receipt_list/", views.ListReceiptBookAPIView.as_view(), name="receipt_list"),
    path("receipt_retrieve/<int:pk>/", views.RetrieveReceiptBookAPIView.as_view(), name="receipt_retrieve"),
    path("return_book/<int:pk>/", views.ReturnBookAPIView.as_view(), name="return_book"),
]
