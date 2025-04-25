import asyncio

from app.core.new_types import UUIDStr


async def join_game(self, game_id: UUIDStr, user_id: int, nickname: str) -> bool:
    lua_script = """
        local meta_key = KEYS[1]
        local players_key = KEYS[2]
        local user_id = ARGV[1]
        local nickname = ARGV[2]
        local max_players = tonumber(ARGV[3])
        
        local status = redis.call('HGET', meta_key, 'status')
        local count = tonumber(redis.call('HGET', meta_key, 'players_count'))
        
        if status ~= 'waiting' or count >= max_players then
            return 0
        end
        
        if redis.call('HEXISTS', players_key, user_id) == 1 then
            return 0
        end
        
        redis.call('HSET', players_key, user_id, nickname)
        redis.call('HINCRBY', meta_key, 'players_count', 1)
        return 1
        """

    result = await self.redis_pool.eval(
        lua_script, 2, f"game:{game_id}:meta", f"game:{game_id}:players", str(user_id), nickname, str(self.MAX_PLAYERS)
    )

    return bool(result)
