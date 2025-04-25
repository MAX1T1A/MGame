from app.core.new_types import UUIDStr


async def check_game_ready(self, game_id: UUIDStr) -> bool:
    lua_script = """
        local players_key = KEYS[1]
        local cursor = 0
        local count = 0
        
        repeat
            local res = redis.call('HSCAN', players_key, cursor, 'MATCH', '*:color')
            cursor = tonumber(res[1])
            
            for i=1, #res[2], 2 do
                if res[2][i+1] == nil then
                    return 0
                end
            end
        until cursor == 0
        
        return 1
        """

    return bool(await self.redis_pool.eval(lua_script, 1, f"game:{game_id}:players"))
