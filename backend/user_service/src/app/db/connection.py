import asyncpg
from app.core.config import user_service_postgres_config
from asyncpg.pool import Pool


async def provide_pool() -> Pool:
    return await asyncpg.create_pool(
        user=user_service_postgres_config.username,
        password=user_service_postgres_config.password,
        database=user_service_postgres_config.dbname,
        host=user_service_postgres_config.host,
        port=user_service_postgres_config.port,
        max_size=user_service_postgres_config.pool_size,
    )
