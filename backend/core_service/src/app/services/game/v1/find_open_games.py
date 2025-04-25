from app.core.new_types import UUIDStr


async def find_open_games(self) -> UUIDStr | None:
    lua_script = """
        local games = redis.call('ZRANGE', 'games:open', 0, 0, 'WITHSCORES')
        if #games == 0 then return nil end
        
        local game_key = games[1]
        local meta_key = game_key..':meta'
        
        local status = redis.call('HGET', meta_key, 'status')
        local count = tonumber(redis.call('HGET', meta_key, 'players_count'))
        
        if status == 'waiting' and count < tonumber(ARGV[1]) then
            return {game_key, count}
        end
        
        return nil
        """

    result = await self.redis_pool.eval(lua_script, 0, str(self.MAX_PLAYERS))
    return result[0].decode().split(":")[1] if result else None
