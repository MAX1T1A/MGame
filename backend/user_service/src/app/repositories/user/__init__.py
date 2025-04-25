from argon2 import PasswordHasher
from asyncpg.pool import Pool

from .v1.authorize import authorize
from .v1.create_one import create_one


class UserRepository:
    def __init__(self, pool: Pool, ph: PasswordHasher):
        self.pool = pool
        self.ph = ph

    authorize = authorize
    create_one = create_one
