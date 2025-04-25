import logging

from app.services.game import GameService
from app.services.providers import provide_game_service_stub
from fastapi import Depends, Query, WebSocket, WebSocketDisconnect


async def play_game(
    websocket: WebSocket,
    user_id: int = Query(..., ge=1),
    nickname: str = Query(...),
    game_service: GameService = Depends(provide_game_service_stub),
):
    await websocket.accept()

    game_id = await game_service.find_open_games()
    if not game_id:
        game_id = await game_service.create_game()

    await websocket.send_text(game_id)

    game = await game_service.join_game(game_id, user_id, nickname)
    if not game:
        await websocket.send_text("Лобби уже заполнено!")
        await websocket.close()

    try:
        while True:
            data = await websocket.receive_json()

            if data["type"] == "select_color":
                success = await game_service.select_color(game_id, user_id, data["color"])
                await websocket.send_json({"type": "color_result", "success": success})

            elif data["type"] == "click":
                x, y = data["x"], data["y"]
                success, color = await game_service.handle_click(game_id, user_id, x, y)
                await websocket.send_json({"type": "click_result", "success": success, "x": x, "y": y})

                if success and color:
                    await game_service.broadcast_to_room(
                        game_id, {"type": "cell_updated", "x": x, "y": y, "color": color, "user_id": user_id}
                    )

    except WebSocketDisconnect:
        await game_service.leave_game(game_id, user_id)
