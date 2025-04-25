from datetime import UTC, datetime

from app.core.new_types import UUIDStr


async def create_game(self) -> UUIDStr:
    game_id = UUIDStr()
    timestamp = int(datetime.now(UTC).timestamp())

    async with self.redis_pool.pipeline() as pipe:
        await pipe.zadd("games:open", {f"game:{game_id}": timestamp})
        await pipe.hset(
            f"game:{game_id}:meta", mapping={"status": "waiting", "created_at": timestamp, "players_count": 0}
        )

        await pipe.hset(f"game:{game_id}:players", "dummy", "")
        await pipe.hdel(f"game:{game_id}:players", "dummy")

        await pipe.hset(f"game:{game_id}:colors", "dummy", "")
        await pipe.hdel(f"game:{game_id}:colors", "dummy")

        await pipe.hset(f"game:{game_id}:scores", "dummy", "0")
        await pipe.hdel(f"game:{game_id}:scores", "dummy")

        await pipe.execute()

    return game_id
