import sys
from django.db.models import Sum
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from lib.weather_tools import manager_get_weather
from shipment.models import Shipment, TRACKING_STATUS_VIEW
import logging


logger = logging.getLogger("process")


@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def get_shipment_data(request, tracking_code):
    try:
        shipment_obj = Shipment.objects.filter(tracking_code=tracking_code).select_related("shipper", "order").first()
        postal_code, country_name = shipment_obj.order.customer.postal_code, shipment_obj.order.customer.country.name
        obj_data = {
            "delivery_date": shipment_obj.delivery_date,
            "shipper": shipment_obj.shipper.brand,
            "status": TRACKING_STATUS_VIEW.get(shipment_obj.status),
            "order": {
                "total_price": shipment_obj.order.orders.values("price_after_discount")
                .aggregate(total_price=Sum("price_after_discount")).get("total_price"),
                "products": shipment_obj.order.orders.values_list("product__name", flat=True),
            },
            "destination_temperature": f"{manager_get_weather(postal_code, country_name)} °C"
        }
        return Response(obj_data)
    except Exception as e:
        message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
        logger.error(message)
        return Response(message)
