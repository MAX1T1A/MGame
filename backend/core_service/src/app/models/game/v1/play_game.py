# import asyncio
# from typing import Literal

# from fastapi import WebSocket
# from pydantic import BaseModel, WebsocketUrl


# class PlayerInGame(BaseModel):
#     user_id: int
#     nickname: str
#     color: str | None = None
#     clicks_total: int = 0
#     clicks_success: int = 0
#     clicks_failed: int = 0
#     score: int = 0
#     is_winner: bool = False


# class Cell(BaseModel):
#     x: int
#     y: int
#     color: str | None = None
#     player_id: int | None = None


# class GameState(BaseModel):
#     id: int
#     status: Literal["waiting", "active", "finished"] = "waiting"
#     players: dict[int, PlayerInGame] = {}
#     field: dict[str, str] = {}  # Ключ: "x_y", значение: цвет
#     websockets: dict[int, WebsocketUrl]
#     countdown_task: None
#     time_left: int = 15


# class Player(BaseModel):
#     user_id: int
#     nickname: str
#     color: str | None = None  # HEX-цвет игрока
#     score: int = 0


# class Cell(BaseModel):
#     x: int
#     y: int
#     color: str


# class PlayerAction(BaseModel):
#     type: Literal["click", "join", "leave"] = "waiting"
#     x: int | None = None
#     y: int | None = None
#     color: str | None = None


# class PlayerDisconnect(BaseModel):
#     message: str = "Пользователь отключился!"
#     code: int = 1000


# class GameMeta(BaseModel):
#     game_id: int
#     status: str  # waiting/active/finished
#     start_time: str | None
#     end_time: str | None


# class Player(BaseModel):
#     user_id: int
#     nickname: str
#     color: str


from typing import Literal

from pydantic import BaseModel


class Player(BaseModel):
    user_id: int
    nickname: str
    color: str | None = None
    score: int = 0


class GameState(BaseModel):
    status: Literal["waiting", "active", "finished"]
    players_count: int
    created_at: int
    players: list[Player]
