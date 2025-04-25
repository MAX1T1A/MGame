from app.repositories.user import UserRepository
from argon2 import PasswordHasher
from asyncpg.pool import Pool


def provide_user_repository_stub():
    raise NotImplementedError


def provide_user_repository(pool: Pool, ph: PasswordHasher) -> UserRepository:
    return UserRepository(pool, ph)
