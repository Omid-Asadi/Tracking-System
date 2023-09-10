from django.db import models
from lib.base_model import BaseModel
from product.models import Product
from user.models import Customer, Retailer


class Order(BaseModel):
    order_date = models.DateTimeField('Order Date', auto_now_add=True, blank=True, null=True)
    seller = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name="seller_orders")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_orders")
    product = models.ManyToManyField(Product, related_name="orders")

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        db_table = "order"

    def __str__(self):
        return f"ID: {self.pk}"
