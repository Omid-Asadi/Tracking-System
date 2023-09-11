import uuid
from django.db import models
from lib.base_model import BaseModel
from order.models import Order


INBOUND_SCAN = 0
SCANNED = 1
IN_TRANSIT = 2
TRANSIT = 3
DELIVERY = 4
TRACKING_STATUS = (
    (INBOUND_SCAN, "InBound Scan"),
    (SCANNED, "Scanned"),
    (IN_TRANSIT, "In Transit"),
    (TRANSIT, "Transit"),
    (DELIVERY, "Delivery"),
)
TRACKING_STATUS_VIEW = {
    INBOUND_SCAN: "InBound Scan",
    SCANNED: "Scanned",
    IN_TRANSIT: "In Transit",
    TRANSIT: "Transit",
    DELIVERY: "Delivery"
}


class Shipper(BaseModel):
    company_name = models.CharField(max_length=128, null=True, blank=True)
    brand = models.CharField(max_length=128)
    website = models.URLField(max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = "shipper"
        verbose_name_plural = "shippers"
        db_table = "shipper"

    def __str__(self):
        return f"{self.brand}"


class Shipment(BaseModel):
    delivery_date = models.DateTimeField("Delivery Date")
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipment")
    shipper = models.ForeignKey(Shipper, on_delete=models.SET_NULL, null=True, blank=True)
    tracking_code = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    status = models.SmallIntegerField(default=0, choices=TRACKING_STATUS)

    class Meta:
        verbose_name = "shipment"
        verbose_name_plural = "shipments"
        db_table = "shipment"

    def __str__(self):
        return f"ID: {self.pk}"
