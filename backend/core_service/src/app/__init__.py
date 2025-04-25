from app.builder import Application
from app.db.connection import provide_pool, provide_redis
from fastapi import FastAPI

app = FastAPI(
    title="Core service",
    version="0.1.0",
    docs_url="/core/api/docs",
    redoc_url="/core/api/redoc",
    openapi_url="/core/api/openapi.json",
)


@app.on_event("startup")
async def initialize_application_resources():
    pool = await provide_pool()
    redis_pool = await provide_redis()
    application_builder = Application(app=app, pool=pool, redis_pool=redis_pool)
    final_application = application_builder.build()

    return final_application.app


@app.on_event("shutdown")
async def shutdown_event():
    # Здесь можно освободить асинхронные ресурсы
    print("Shutdown event")
