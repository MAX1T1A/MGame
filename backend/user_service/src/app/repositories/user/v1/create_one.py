import asyncpg


async def create_one(self, data: dict[str, str]) -> None | Exception:
    query = """
            INSERT INTO users (nickname, password_hash)
            VALUES ($1, $2);
            """
    hash_password = self.ph.hash(data["password"])

    async with self.pool.acquire() as connection:
        try:
            return await connection.execute(query, data["nickname"], hash_password)
        except asyncpg.exceptions.UniqueViolationError:
            raise
