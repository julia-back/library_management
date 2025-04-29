from celery import shared_task
from .models import ReceiptBook
from datetime import date, timedelta, datetime, time
from django.core.cache import cache
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.utils import timezone


@shared_task
def send_notification_by_return_book():

    queryset = cache.get("receipt_queryset_all")
    if queryset is None:
        queryset = ReceiptBook.objects.all()
        cache.set("receipt_queryset_all", queryset, 60 * 5)

    for receipt in queryset:
        if receipt.return_date is None:

            current_period = date.today() - receipt.receipt_date
            remaining_days = timedelta(days=receipt.period_in_days) - current_period

            if remaining_days < timedelta(days=0):
                send_mail(subject="Необходимо сдать книгу!",
                          message="Период взятия книги истек. Подробнее можно ознакомиться в личном кабинете.",
                          from_email=EMAIL_HOST_USER, recipient_list=[receipt.user.email])

            if remaining_days <= timedelta(days=2):
                send_mail(subject="Не забудьте сдать книгу.",
                          message="Период взятия книги скоро закончится. "
                                  "Подробнее можно ознакомиться в личном кабинете.",
                          from_email=EMAIL_HOST_USER, recipient_list=[receipt.user.email])
