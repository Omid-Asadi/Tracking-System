from django.contrib import admin
from django.urls import path, include
from shipment import urls as shipment_url


urlpatterns = [
    path("admin/", admin.site.urls),
    path("shipment/", include(shipment_url)),
]
