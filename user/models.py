from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from lib.base_model import BaseModel


class CustomUser(AbstractUser):
    postal_code = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=32)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"ID: {self.pk}"
