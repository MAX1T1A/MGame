import logging
import os

from app.api.http.game import game_router_v1
from app.repositories.providers import (
    provide_game_repository,
    provide_game_repository_stub,
)
from app.services.providers import provide_game_service, provide_game_service_stub
from asyncpg.pool import Pool
from fastapi import FastAPI
from redis.asyncio import Redis


class Application:
    def __init__(self, app: FastAPI, pool: Pool, redis_pool: Redis):
        self.app = app
        self.pool = pool
        self.redis_pool = redis_pool

        self.logger = logging.getLogger(self.__class__.__name__)

    def _create_repositories(self):
        self.game_repository = provide_game_repository(self.pool)

    def _create_services(self):
        self.game_service = provide_game_service(self.game_repository, self.redis_pool)

    def _override_dependencies(self):
        self.app.dependency_overrides = {
            provide_game_repository_stub: lambda: self.game_repository,
            provide_game_service_stub: lambda: self.game_service,
        }

    def _add_routes(self):
        self.app.include_router(game_router_v1)

    def _configure_logging(self):
        logging.basicConfig(
            level=int(os.environ["LOGGING_LEVEL"]),
            format="%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s",
        )

    def build(self):
        self._create_repositories()
        self._create_services()
        self._override_dependencies()
        self._add_routes()
        self._configure_logging()

        return self
