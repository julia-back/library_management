from django.db import models


class Author(models.Model):
    """Класс модели автора."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)


class Book(models.Model):
    """Класс модели книги. Имеет связанное поле автора (многие-ко-многим)."""

    language_choices = {
        "eng": "Английский",
        "ru": "Русский",
    }

    status_choices = {
        "free": "Доступна для выдачи",
        "on_hands": "Выдана на руки",
    }

    serial_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    author = models.ManyToManyField(Author)
    genre = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=language_choices)
    publishing_house = models.CharField(max_length=255, blank=True, null=True)
    place_of_publication = models.CharField(max_length=50, blank=True, null=True)
    publication_year = models.PositiveIntegerField(max_length=4, blank=True, null=True)
    receipt_status = models.CharField(max_length=10, choices=status_choices, default="free")
