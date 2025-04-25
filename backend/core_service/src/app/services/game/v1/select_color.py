from app.core.new_types import UUIDStr


async def select_color(self, game_id: UUIDStr, user_id: int, color: str) -> bool:
    lua_script = """
        local colors_key = KEYS[1]
        local user_id = ARGV[1]
        local new_color = ARGV[2]
        
        -- Если ключа colors нет -> создаем его
        if redis.call('EXISTS', colors_key) == 0 then
            redis.call('HSET', colors_key, user_id, new_color)
            return 1
        end
        
        -- Проверка уникальности цвета
        local all_colors = redis.call('HVALS', colors_key)
        for _, c in ipairs(all_colors) do
            if c == new_color then return 0 end
        end
        
        -- Обновляем цвет
        redis.call('HSET', colors_key, user_id, new_color)
        return 1
        """
    return bool(await self.redis_pool.eval(lua_script, 1, f"game:{game_id}:colors", str(user_id), color))
