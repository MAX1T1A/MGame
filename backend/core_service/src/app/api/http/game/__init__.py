from app.api.http.game.v1.play_game import play_game
from fastapi import APIRouter, status

game_router_v1 = APIRouter(tags=["Game"], prefix="/core/api/v1")


game_router_v1.add_api_websocket_route("/game", play_game)
