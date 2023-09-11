from django.urls import path
from shipment.api.views import get_shipment_data


urlpatterns = [
    path("get-shipment/<str:tracking_code>", get_shipment_data, name="get_shipment_data"),
]
