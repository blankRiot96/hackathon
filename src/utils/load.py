import typing as t
from functools import lru_cache

import pygame


@lru_cache
def load_font(file_name: str | None, size: int) -> pygame.font.Font:
    return pygame.font.Font(file_name, size)
