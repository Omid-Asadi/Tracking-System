from django.db import models

from lib.base_model import BaseModel
from user.models import CustomUser


class Order(BaseModel):
    order_date = models.DateTimeField('Order Date', auto_now_add=True, blank=True, null=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender_orders")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="receiver_orders")

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        db_table = "order"

    def __str__(self):
        return f"ID: {self.pk}"
