from asyncpg.pool import Pool

from .v1.find_by_id import find_by_id
from .v1.find_open_game import find_open_game


class GameRepository:
    def __init__(self, pool: Pool):
        self.pool = pool

    find_by_id = find_by_id
    find_open_game = find_open_game
