import asyncio

from app.core.new_types import UUIDStr


async def track_game_progress(self, game_id: UUIDStr):
    total_cells = 100  # 10x10 grid
    while True:
        filled = await self.redis_pool.hlen(f"game:{game_id}:grid")
        if filled >= total_cells:
            await self.finish_game(game_id)
            break
        await asyncio.sleep(1)
