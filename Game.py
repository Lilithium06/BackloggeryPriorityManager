from dataclasses import dataclass
from typing import Optional

@dataclass
class Game:
    unique_game_id: int
    title: str
    platform: str
    sub_platform: Optional[str]
    status: str
    priority: str
    format: Optional[str]
    ownership: Optional[str]
    notes: Optional[str]
    child_of: Optional[int]
    last_updated: str