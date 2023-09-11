from django.db import models
from lib.base_model import BaseModel
from product.models import Product
from user.models import Customer, Retailer


class Order(BaseModel):
    order_date = models.DateTimeField('Order Date', auto_now_add=True, blank=True, null=True)
    seller = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name="seller_orders")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer_orders")
    product = models.ManyToManyField(Product, related_name="orders", through="OrderProduct")

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        db_table = "order"

    def __str__(self):
        return f"ID: {self.pk}"


class OrderProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")
    price_after_discount = models.FloatField("Final Price")
    quantity = models.IntegerField("Quantity", default=1)

    class Meta:
        verbose_name = "order product"
        verbose_name_plural = "order products"
        db_table = "order_product"

    def __str__(self):
        return f"ID: {self.pk}"
