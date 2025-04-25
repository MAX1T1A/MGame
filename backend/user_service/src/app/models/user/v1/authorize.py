from app.models.user import Base
from pydantic import BaseModel

HTTP_404_NOT_FOUND_DETAIL = "Пользователь с таким логином не найден!"
HTTP_400_BAD_REQUEST_DETAIL = "Неправильный логин или пароль!"


class AuthorizeRequest(Base): ...


class AuthorizeResponse(BaseModel):
    id: int
    nickname: str
