from django.core.management.base import BaseCommand
from django.db import transaction

from accounts import models, signals


class Command(BaseCommand):
    help = "Generates initial data and inserts them into database"

    def handle(self, *args, **options):
        with transaction.atomic():
            self.create_admin()

    @staticmethod
    def create_admin():
        email = "admin@example.com"
        if models.User.objects.filter(username__iexact=email).exists():
            return False

        user = models.User.objects.create_superuser(email, email, "demo12345")
        signals.user_signup.send("fitapp", user=user)

        return user
