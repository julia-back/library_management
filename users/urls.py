from django.urls import path
from .apps import UsersConfig
from . import views


app_name = UsersConfig.name

urlpatterns = [
    path("token/", views.UserTokenObtainPairView.as_view(), name="token_pair"),
    path("token_refresh/", views.UserTokenRefreshView.as_view(), name="token_refresh"),

    path("user/new/", views.UserCreateAPIView.as_view(), name="user_create"),
    path("user_list/", views.UserListAPIView.as_view(), name="user_list"),
    path("user_retrieve/<int:pk>/", views.UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user_update/<int:pk>/", views.UserUpdateAPIView.as_view(), name="user_update"),
    path("user_destroy/<int:pk>/", views.UserDestroyAPIView.as_view(), name="user_destroy"),

    path("add_in_admin_group/<int:pk>/", views.AddUserInAdminGroup.as_view(), name="add_in_admin")
]
