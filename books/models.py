from django.db import models


class Author(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic_name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)


class Book(models.Model):

    language_choices = {
        "eng": "Английский",
        "ru": "Русский",
    }

    status_choices = {
        "free": "Доступна для выдачи",
        "on_hands": "Выдана на руки",
    }

    serial_number = models.CharField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    author = models.ManyToManyField(Author)
    genre = models.CharField(max_length=255)
    language = models.CharField(choices=language_choices)
    publishing_house = models.CharField(max_length=255)
    place_of_publication = models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField(max_length=4)
    receipt_status = models.CharField(choices=status_choices, default="free")
