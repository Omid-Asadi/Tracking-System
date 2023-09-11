import redis
from tracking.business_rules import REDIS_EXPIRE_TIME
from tracking.local_settings import REDIS_WEATHER_DATA_DB_NUMBER, REDIS_PORT, REDIS_ADDRESS
import logging


logger = logging.getLogger("process")


class RedisClient:
    _instance = None

    def __init__(self, host, port, db, *args, **kwargs):
        self.host, self.port, self.db = host, port, db
        self._pool = redis.Redis(host=self.host, port=self.port, db=self.db, decode_responses=True)

    def __new__(cls, host, port, db, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def get_connection(self):
        return self._pool

    def get_data_from_redis(self, key):
        try:
            client = self.get_connection()
            return int(client.get(key))
        except Exception as e:
            message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
            logger.error(message)
            return False

    def set_data_into_redis(self, key, value, exp=None):
        try:
            client = self.get_connection()
            client.set(key, value, REDIS_EXPIRE_TIME)
        except Exception as e:
            message = f"message: {str(e)} | line no:{sys.exc_info()[2].tb_lineno}"
            logger.error(message)
            return False


redis_obj = RedisClient(REDIS_ADDRESS, REDIS_PORT, REDIS_WEATHER_DATA_DB_NUMBER)
