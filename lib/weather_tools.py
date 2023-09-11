import logging
import sys

import pgeocode
import requests
from rest_framework import status
from lib.redis_tools import RedisClient
from tracking.business_rules import WEATHER_API_KEY, WEATHER_PERIOD_IN_HOUR, WEATHER_API, REDIS_EXPIRE_TIME
import country_converter as coco
from tracking.local_settings import REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER


logger = logging.getLogger("process")


def manager_get_weather(postal_code, country_name):
    try:
        redis_obj = RedisClient(REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER)
        redis_key = f"{country_name}_{postal_code}"
        result = redis_obj.get_data_from_redis(redis_key)
        if not result:
            result = get_weather_data_from_reference(postal_code, country_name)
            redis_obj.set_data_into_redis(redis_key, result)
        return result
    except Exception as e:
        message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
        logger.error(message)
        return False


def get_weather_data_from_reference(postal_code, country_name, count=3):
    try:
        iso2_country = convert_country_name_to_iso2(country_name)
        lat, long = get_lat_long_from_postal(postal_code, iso2_country)
        url = WEATHER_API.format(WEATHER_API_KEY, lat, long)
        res = requests.request("get", url)
        if res.status_code == status.HTTP_200_OK:
            res = res.json()
            return res.get("data")[0].get('temp')
        if count > 0:
            return get_weather_data_from_reference(postal_code, country_name, count=count-1)
        return False
    except Exception as e:
        if count > 0:
            return get_weather_data_from_reference(postal_code, country_name, count=count-1)
        message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
        logger.error(message)
        return False


def get_lat_long_from_postal(postal_code, country_iso2):
    try:
        client = pgeocode.Nominatim(country_iso2)
        result = client.query_postal_code(postal_code)
        return result.get('latitude'), result.get('longitude')
    except Exception as e:
        message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
        logger.error(message)
        return False


def convert_country_name_to_iso2(country, output_type="ISO2"):
    try:
        return coco.convert(names=country, to=output_type)
    except Exception as e:
        message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
        logger.error(message)
        return False
