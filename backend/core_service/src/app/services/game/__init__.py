import asyncio
import json
import logging
import uuid
from datetime import UTC, datetime, time
from typing import Literal

from app.core.new_types import UUIDStr
from app.repositories.game import GameRepository
from fastapi import WebSocket
from pydantic import BaseModel
from redis.asyncio import Redis, WatchError

from .v1.broadcast import broadcast
from .v1.check_game_ready import check_game_ready
from .v1.create_game import create_game
from .v1.find_game_status import find_game_status
from .v1.find_open_games import find_open_games
from .v1.finish_game import finish_game
from .v1.handle_click import handle_click
from .v1.join_game import join_game
from .v1.leave_game import leave_game
from .v1.select_color import select_color
from .v1.track_game_progress import track_game_progress


class GameService:
    def __init__(self, game_repository: GameRepository, redis_pool: Redis):
        self.game_repository = game_repository
        self.redis_pool = redis_pool
        self.MAX_PLAYERS = 4

    broadcast = broadcast
    check_game_ready = check_game_ready
    create_game = create_game
    find_game_status = find_game_status
    find_open_games = find_open_games
    finish_game = finish_game
    handle_click = handle_click
    join_game = join_game
    leave_game = leave_game
    select_color = select_color
    track_game_progress = track_game_progress
