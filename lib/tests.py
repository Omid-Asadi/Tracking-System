from unittest import TestCase
from lib.redis_tools import RedisClient
from tracking.local_settings import REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER


class ShipmentTestCase(TestCase):
    def setUp(self):
        RedisClient(REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER)

    def test_redis_connection(self):
        obj = RedisClient(REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER)
        connection = obj.get_connection()
        self.assertIsNotNone(connection)

    def test_redis_setter(self):
        obj = RedisClient(REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER)
        obj.set_data_into_redis(1, 2)
        self.assertTrue(isinstance(obj.get_data_from_redis(1), int))
