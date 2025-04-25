import asyncio

from app.core.new_types import UUIDStr


async def start_countdown(self, game_id: UUIDStr):
    for i in range(15, 0, -1):
        await self.broadcast(game_id, {"type": "countdown", "value": i})
        await asyncio.sleep(1)

    meta = await self.redis_pool.hgetall(f"game:{game_id}:meta")
    if meta.get(b"status") == b"waiting" and int(meta.get(b"players_count", 0)) >= self.MAX_PLAYERS:
        await self.start_game(game_id)
