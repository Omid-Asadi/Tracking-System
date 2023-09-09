from django.contrib import admin
from shipment.models import Shipper, Tracking, Shipment


admin.site.register(Shipper)
admin.site.register(Tracking)
admin.site.register(Shipment)

