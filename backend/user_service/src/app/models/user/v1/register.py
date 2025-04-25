from app.models.user import Base
from pydantic import Field

HTTP_400_BAD_REQUEST_DETAIL = "Пользователь с таким ником уже существует!"


class RegisterRequest(Base): ...
