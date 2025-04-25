from app.repositories.game import GameRepository
from app.services.game import GameService
from redis.asyncio import Redis


def provide_game_service_stub():
    raise NotImplementedError


def provide_game_service(game_repository: GameRepository, redis_pool: Redis) -> GameService:
    return GameService(game_repository, redis_pool)
