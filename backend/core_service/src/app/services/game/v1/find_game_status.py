from app.core.new_types import UUIDStr
from app.models.game.v1.play_game import GameState


async def find_game_status(self, game_id: UUIDStr) -> GameState:
    meta_data = await self.redis_pool.hgetall(f"game:{game_id}:meta")
    if not meta_data:
        raise ValueError("Game not found")

    players = await self.redis_pool.hgetall(f"game:{game_id}:players")
    colors = await self.redis_pool.hgetall(f"game:{game_id}:colors")
    scores = await self.redis_pool.hgetall(f"game:{game_id}:scores")

    return GameState(
        status=meta_data.get(b"status", "waiting").decode(),
        players_count=int(meta_data.get(b"players_count", 0)),
        created_at=int(meta_data.get(b"created_at", 0)),
        players=[],
    ).model_dump_json()
