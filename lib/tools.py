import requests
from tracking.business_rules import WEATHER_URL


def get_weather_data(postal_code):
    requests.request("get", WEATHER_URL)