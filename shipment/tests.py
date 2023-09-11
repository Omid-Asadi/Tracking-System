from unittest import TestCase
from requests import Response
from rest_framework import status
from django.test import Client
from django.urls import reverse


class ShipmentTestCase(TestCase):
    def test_shipment_url_checker(self):
        client = Client()
        response = client.get(reverse('get_shipment_data', kwargs={"tracking_code": "test"}))
        self.assertIsInstance(type(response), type(Response))

    def test_shipment_url_type(self):
        client = Client()
        response = client.get(reverse('get_shipment_data', kwargs={"tracking_code": "test"}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
