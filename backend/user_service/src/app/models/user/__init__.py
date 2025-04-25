from pydantic import BaseModel, Field


class Base(BaseModel):
    nickname: str = Field(..., max_length=50, example="max1t1a")
    password: str = Field(..., min_length=8, example="strongpassword123")
