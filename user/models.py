from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.db import models

from lib.base_model import BaseModel

USA = 0
AUSTRALIA = 1

COUNTRIES = (
    (USA, "USA"),
    (AUSTRALIA, "AUSTRALIA"),
)


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    address = models.OneToOneField("Address", on_delete=models.SET_NULL, related_name="customer")

    # country = CountryField()
    # address = models.TextField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer"
        db_table = "customer"

    def __str__(self):
        return f"ID: {self.pk}"


class Retailer(Customer):
    # country = CountryField()
    seller_rate = models.SmallIntegerField("Rate", blank=True, null=True)
    seller_lead_time = models.FloatField("Seller Lead Time", blank=True, null=True)
    address = models.OneToOneField("Address", on_delete=models.SET_NULL, related_name="customer")

    class Meta:
        verbose_name = "Retailer"
        verbose_name_plural = "Retailers"
        db_table = "retailer"

    def __str__(self):
        return f"ID: {self.pk}"


class Address(models.Model):
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('cities_light.City', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=100)
