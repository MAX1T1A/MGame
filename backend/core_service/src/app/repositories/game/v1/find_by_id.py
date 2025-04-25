import logging


async def find_by_id(self, game_id: int) -> int | None:
    query_select = """
            SELECT g.id
            FROM games g
            LEFT JOIN game_players gp ON g.id = gp.game_id
            WHERE g.status = 'waiting'
                AND g.id = $1
            GROUP BY g.id
            HAVING COUNT(gp.id) < 4
            LIMIT 1;
            """

    async with self.pool.acquire() as connection:
        async with connection.transaction():
            game_id = await connection.fetchval(query_select, game_id)
            return game_id
