from app.core.new_types import UUIDStr


async def handle_click(self, game_id: UUIDStr, user_id: int, x: int, y: int) -> bool:
    lua_script = """
        local grid_key = KEYS[1]
        local colors_key = KEYS[2]
        local scores_key = KEYS[3]
        local user_id = ARGV[1]
        local coords = ARGV[2]
        
        -- Проверяем наличие цвета (если ключа нет -> возвращаем 0)
        if redis.call('EXISTS', colors_key) == 0 then return 0 end
        local color = redis.call('HGET', colors_key, user_id)
        if not color then return 0 end
        
        -- Захват ячейки (если поле не существует)
         if redis.call('HSETNX', grid_key, coords, color) == 1 then
            redis.call('HINCRBY', scores_key, user_id, 1)
            return {1, color} 
        end
        return {0}
        """
    result = await self.redis_pool.eval(
        lua_script,
        3,
        f"game:{game_id}:grid",
        f"game:{game_id}:colors",
        f"game:{game_id}:scores",
        str(user_id),
        f"{x},{y}",
    )

    if result and result[0] == 1:
        return True, result[1].decode()
    return False, None
