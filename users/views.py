from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import UserSerializer, UserCreateSerializer
from .models import User
from django.contrib.auth.models import Group
from rest_framework import generics, views
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.permissions import IsAdmin, IsCurrentUser
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from rest_framework import status


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
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        """
        Метод создания пользователя. Устанавливает захешированный пароль.
        """
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """
    Представление для предоставления списка пользователей.
    Доступно только пользователям, состоящим в группе администраторов.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = cache.get("user_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("user_queryset_all", queryset, 60 * 5)
        return queryset


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Представление для предоставления деталей пользователя. Доступно
    пользователям, состоящим в группе администраторов, и пользователям,
    получающим свой объект пользователя.
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsCurrentUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = cache.get("user_queryset_all")
        if queryset is None:
            queryset = super().get_queryset()
            cache.set("user_queryset_all", queryset, 60 * 5)
        return queryset


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


class AddUserInAdminGroup(views.APIView):
    """
    Представление добавления пользователя в группу admin.
    Доступно только пользователям, состоящим в группе администраторов.
    """

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            admin_group, created = Group.objects.get_or_create(name="admin")
            user = User.objects.get(pk=kwargs.get("pk"))

            if user.groups.filter(name="admin").exists():
                return Response(data={"comment": "User already in admin group 'admin'."},
                                status=status.HTTP_400_BAD_REQUEST)

            user.groups.add(admin_group)
            return Response(data={"comment": "User successfully added in group 'admin'."},
                            status=status.HTTP_200_OK)
        except NotFound:
            return Response(data={"comment": "User not found."},
                            status=status.HTTP_400_BAD_REQUEST)
