from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.permissions import IsAdmin, IsCurrentUser
from rest_framework.permissions import IsAuthenticated


class UserTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]


class UserTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsCurrentUser]
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsCurrentUser]
    serializer_class = UserSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsCurrentUser]
    serializer_class = UserSerializer
