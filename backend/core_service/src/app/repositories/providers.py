from app.repositories.game import GameRepository
from asyncpg.pool import Pool


def provide_game_repository_stub():
    raise NotImplementedError


def provide_game_repository(pool: Pool) -> GameRepository:
    return GameRepository(pool)
