import logging
import os

from app.api.http.user import user_router_v1
from app.repositories.providers import (
    provide_user_repository,
    provide_user_repository_stub,
)
from argon2 import PasswordHasher
from asyncpg.pool import Pool
from fastapi import FastAPI


class Application:
    def __init__(self, app: FastAPI, pool: Pool, ph: PasswordHasher):
        self.app = app
        self.pool = pool
        self.ph = ph
        self.logger = logging.getLogger(self.__class__.__name__)

    def _create_repositories(self):
        self.user_repository = lambda: provide_user_repository(self.pool, self.ph)

    def _create_services(self): ...

    def _override_dependencies(self):
        self.app.dependency_overrides = {provide_user_repository_stub: self.user_repository}

    def _add_routes(self):
        self.app.include_router(user_router_v1)

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
