from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

username_validator = UnicodeUsernameValidator()


class Customer(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField('email address', unique=True)
    avatar = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=32, blank=True, null=True, unique=True)
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    postal_code = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"
        db_table = "customer"

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return f"ID: {self.pk}"


class Retailer(Customer):
    seller_rate = models.SmallIntegerField("Rate", blank=True, null=True)
    seller_lead_time = models.FloatField("Seller Lead Time", blank=True, null=True)

    class Meta:
        verbose_name = "Retailer"
        verbose_name_plural = "Retailers"
        db_table = "retailer"

    def __str__(self):
        return f"ID: {self.pk}"
