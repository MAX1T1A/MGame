import os

from app.core.config.postgres import PostgresConfig
from app.core.config.reids import RedisConfig

core_service_postgres_config = PostgresConfig(
    host=os.environ["POSTGRES_DB_HOST"],
    port=int(os.environ["POSTGRES_DB_PORT"]),
    username=os.environ["POSTGRES_DB_LOGIN"],
    password=os.environ["POSTGRES_DB_PASSWORD"],
    dbname=os.environ["POSTGRES_DB_NAME"],
    pool_size=int(os.environ["SQLALCHEMY_POOL_SIZE"]),
)

core_service_redis_config = RedisConfig(url=os.environ["REDIS_URL"])
