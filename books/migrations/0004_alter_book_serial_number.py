# Generated by Django 5.2 on 2025-04-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_alter_book_language_alter_book_receipt_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="serial_number",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
