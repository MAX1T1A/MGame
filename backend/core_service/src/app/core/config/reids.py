import os
from dataclasses import dataclass


@dataclass
class RedisConfig:
    url: str
