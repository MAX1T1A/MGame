import asyncpg
from argon2.exceptions import InvalidHashError


async def authorize(self, data: dict[str, str]) -> dict:
    query = """
            SELECT id, nickname, password_hash FROM users WHERE nickname = $1;
            """

    async with self.pool.acquire() as connection:
        try:
            user = await connection.fetchrow(query, data["nickname"])
            try:
                self.ph.verify(user["password_hash"], data["password"])
                return {"id": user["id"], "nickname": data["nickname"]}
            except InvalidHashError as e:
                raise
        except asyncpg.exceptions.NoDataFoundError as e:
            raise
