from django.db import models
from lib.base_model import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=128)
    price = models.FloatField("price")
    sku = models.CharField(max_length=32)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "product"

    def __str__(self):
        return f"{self.name}"
