from app.builder import Application
from app.db.connection import provide_pool
from argon2 import PasswordHasher
from fastapi import FastAPI

app = FastAPI(
    title="User service",
    version="0.1.0",
    docs_url="/user/api/docs",
    redoc_url="/user/api/redoc",
    openapi_url="/user/api/openapi.json",
)


@app.on_event("startup")
async def initialize_application_resources():
    pool = await provide_pool()
    ph = PasswordHasher()

    application_builder = Application(app=app, pool=pool, ph=ph)
    final_application = application_builder.build()

    return final_application.app


@app.on_event("shutdown")
async def shutdown_event():
    # Здесь можно освободить асинхронные ресурсы
    print("Shutdown event")
