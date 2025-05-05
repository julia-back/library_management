from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User
import os
from dotenv import load_dotenv
import logging


load_dotenv()
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ("Команда создает или получает группу admin, создает или "
            "получает пользователя и добавляет в группу.")

    def handle(self, *args, **options):
        admin_group, created = Group.objects.get_or_create(name="admin")
        admin_user, created = User.objects.get_or_create(email=os.getenv("ADMIN_USER_EMAIL"),
                                                         username=os.getenv("ADMIN_USER_USERNAME"))
        admin_user.set_password(os.getenv("ADMIN_USER_PASSWORD"))
        admin_user.save()
        if not admin_user.groups.filter(name="admin").exists():
            admin_user.groups.add(admin_group)
