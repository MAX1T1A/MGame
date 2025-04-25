import asyncpg
from app.core.config import core_service_postgres_config, core_service_redis_config
from asyncpg.pool import Pool
from redis.asyncio import ConnectionPool, Redis


async def provide_pool() -> Pool:
    return await asyncpg.create_pool(
        user=core_service_postgres_config.username,
        password=core_service_postgres_config.password,
        database=core_service_postgres_config.dbname,
        host=core_service_postgres_config.host,
        port=core_service_postgres_config.port,
        max_size=core_service_postgres_config.pool_size,
    )


async def provide_redis() -> Redis:
    pool = ConnectionPool.from_url(core_service_redis_config.url)
    return Redis(connection_pool=pool, encoding="utf-8")
