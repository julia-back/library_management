from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User
import os
from dotenv import load_dotenv


load_dotenv()


class Command(BaseCommand):
    help = ("Команда создает или получает группу admin, создает или "
            "получает пользователя и добавляет в группу.")

    def handle(self, *args, **options):
        admin_group = Group.objects.get_or_create(name="admin")
        admin_user = User.objects.get_or_create(email=os.getenv("ADMIN_USER_EMAIL"),
                                                username=os.getenv("ADMIN_USER_USERNAME"),
                                                password=os.getenv("ADMIN_USER_PASSWORD"))
        admin_user.group_set.add(admin_group)
