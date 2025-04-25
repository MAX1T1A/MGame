import logging

from app.core.new_types import UUIDStr


async def broadcast(self, game_id: UUIDStr, message: dict):
    if game_id in self.active_websockets:
        for ws in self.active_websockets[game_id]:
            try:
                await ws.send_json(message)
            except Exception as e:
                logging.error(f"Broadcast error: {e}")
