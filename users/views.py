from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.permissions import IsAdmin, IsCurrentUser
from rest_framework.permissions import IsAuthenticated


class UserTokenObtainPairView(TokenObtainPairView):
    """
    Представление для получения токенов.
    Доступно неавторизованным пользователям.
    """

    permission_classes = [AllowAny]


class UserTokenRefreshView(TokenRefreshView):
    """
    Представление для обновления токенов.
    Доступно неавторизованным пользователям.
    """

    permission_classes = [AllowAny]


class UserCreateAPIView(generics.CreateAPIView):
    """
    Представление для создания / регистрации пользователя.
    Доступно неавторизованным пользователям.
    """

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    Представление для предоставления списка пользователей.
    Доступно только пользователям, состоящим в группе администраторов.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для предоставления деталей пользователя. Доступно
    пользователям, состоящим в группе администраторов, и пользователям,
    получающим свой объект пользователя.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsCurrentUser]
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Представление для обновления пользователя.
    Доступно пользователям, получающим свой объект пользователя.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsCurrentUser]
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    Представление для удаления пользователя.
    Доступно пользователям, получающим свой объект пользователя.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsCurrentUser]
    serializer_class = UserSerializer
