from app.models.user.v1.register import HTTP_400_BAD_REQUEST_DETAIL, RegisterRequest
from app.repositories.providers import (
    provide_user_repository_stub,
)
from app.repositories.user import UserRepository
from fastapi import Depends, HTTPException, Response, status


async def register(
    request: RegisterRequest, user_repository: UserRepository = Depends(provide_user_repository_stub)
) -> Response:
    try:
        await user_repository.create_one(request.model_dump())
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=HTTP_400_BAD_REQUEST_DETAIL) from e
