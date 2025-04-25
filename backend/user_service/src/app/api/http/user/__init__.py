from app.api.http.user.v1.authorize import authorize
from app.api.http.user.v1.register import register
from app.models.user.v1.authorize import AuthorizeResponse
from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse

user_router_v1 = APIRouter(tags=["User"], prefix="/user/api/v1")

user_router_v1.add_api_route(
    "/authorize", authorize, methods=["POST"], response_model=AuthorizeResponse, status_code=status.HTTP_200_OK
)

user_router_v1.add_api_route(
    "/register", register, methods=["POST"], response_class=Response, status_code=status.HTTP_201_CREATED
)
