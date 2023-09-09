import logging
import pgeocode
import requests
from tracking.business_rules import WEATHER_URL


logger = logging.getLogger("process")


def get_weather_data(postal_code):
    try:
        lat, long = get_lat_long_from_postal(postal_code)
        res = requests.request("get", WEATHER_URL)
    except Exception as e:
        pass


def get_lat_long_from_postal(postal_code, country=None):
    try:
        nomi = pgeocode.Nominatim(country)
        result = nomi.query_postal_code(postal_code)
        return result.get('latitude'), result.get('longitude')
    except Exception as e:
        pass
