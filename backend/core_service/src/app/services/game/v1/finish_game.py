from app.core.new_types import UUIDStr


async def finish_game(self, game_id: UUIDStr):
    lua_script = """
        local scores_key = KEYS[1]
        local meta_key = KEYS[2]
        local players_key = KEYS[3]
        
        -- Находим победителя
        local scores = redis.call('HGETALL', scores_key)
        local max_score = -1
        local winner = nil
        
        for i=1, #scores, 2 do
            local current = tonumber(scores[i+1])
            if current > max_score then
                max_score = current
                winner = scores[i]
            end
        end
        
        if winner then
            redis.call('HSET', players_key, winner..':is_winner', 1)
        end
        
        redis.call('HSET', meta_key, 'status', 'finished')
        return winner or ''
        """

    winner_id = await self.redis_pool.eval(
        lua_script, 3, f"game:{game_id}:scores", f"game:{game_id}:meta", f"game:{game_id}:players"
    )

    if winner_id:
        await self.cleanup_game(game_id)
