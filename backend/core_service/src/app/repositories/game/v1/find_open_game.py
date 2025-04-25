async def find_open_game(self) -> int:
    query_select = """
            SELECT g.id
            FROM games g
            LEFT JOIN game_players gp ON g.id = gp.game_id
            WHERE g.status = 'waiting'
            GROUP BY g.id
            HAVING COUNT(gp.id) < 4
            LIMIT 1;
            """

    query_insert = """
            INSERT INTO games (status) VALUES ('waiting') RETURNING id;
            """

    async with self.pool.acquire() as connection:
        async with connection.transaction():
            game_id = await connection.fetchval(query_select)
            if not game_id:
                game_id = await connection.fetchval(query_insert)

            return game_id
