from app.models.user.v1.authorize import (
    HTTP_400_BAD_REQUEST_DETAIL,
    HTTP_404_NOT_FOUND_DETAIL,
    AuthorizeRequest,
    AuthorizeResponse,
)
from app.repositories.providers import (
    provide_user_repository_stub,
)
from app.repositories.user import UserRepository
from fastapi import Depends, HTTPException, status


async def authorize(
    request: AuthorizeRequest, user_repository: UserRepository = Depends(provide_user_repository_stub)
) -> AuthorizeResponse:
    try:
        data = await user_repository.authorize(request.model_dump())
        return AuthorizeResponse(**data)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=HTTP_400_BAD_REQUEST_DETAIL) from e
