# Generated by Django 5.2 on 2025-04-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="receipt_status",
            field=models.CharField(
                choices=[("free", "Доступна для выдачи"), ("on_hands", "Выдана на руки")], default="free"
            ),
        ),
    ]
