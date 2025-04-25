from app.core.new_types import UUIDStr


async def leave_game(self, game_id: UUIDStr, user_id: int) -> bool:
    lua_script = """
        local meta_key = KEYS[1]
        local players_key = KEYS[2]
        local grid_key = KEYS[3]
        local colors_key = KEYS[4]
        local scores_key = KEYS[5]
        local game_zset_key = KEYS[6]
        
        local user_id = ARGV[1]
        
        if redis.call('HGET', meta_key, 'status') ~= 'waiting' then
            return 0
        end
        
        local deleted = redis.call('HDEL', players_key, user_id)
        if deleted == 0 then
            return 0
        end
        
        local new_count = redis.call('HINCRBY', meta_key, 'players_count', -1)
        
        if new_count <= 0 then
            redis.call('DEL', meta_key, players_key, grid_key, colors_key, scores_key)
            redis.call('ZREM', 'games:open', game_zset_key)
        end
        
        return 1
        """

    return bool(
        await self.redis_pool.eval(
            lua_script,
            6,
            f"game:{game_id}:meta",
            f"game:{game_id}:players",
            f"game:{game_id}:grid",
            f"game:{game_id}:colors",
            f"game:{game_id}:scores",
            f"game:{game_id}",
            str(user_id),
        )
    )
