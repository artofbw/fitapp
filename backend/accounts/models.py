from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    height = models.IntegerField("height", null=True)

    def __str__(self):
        return self.email
