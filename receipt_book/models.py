from django.db import models
from users.models import User
from books.models import Book


class ReceiptBook(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET("book_deleted"))
    receipt_date = models.DateField(auto_now_add=True)
    period_in_days = models.PositiveIntegerField(default=7)
    return_date = models.DateField(blank=True, null=True)
