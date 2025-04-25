from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Класс модели пользователя. Определяет поле email полем авторизации,
    сохраняет поле username обязательным полем.
    """

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"
