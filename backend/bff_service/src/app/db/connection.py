import asyncpg

from app.core.config import metabrain_postgres_config


async def provide_pool() -> asyncpg.pool.Pool:
    return await asyncpg.create_pool(
        user=metabrain_postgres_config.username,
        password=metabrain_postgres_config.password,
        database=metabrain_postgres_config.dbname,
        host=metabrain_postgres_config.host,
        port=metabrain_postgres_config.port,
        max_size=metabrain_postgres_config.pool_size,
    )
