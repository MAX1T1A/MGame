from pydantic import BaseModel, Field


class Base(BaseModel):
    game_id: int
