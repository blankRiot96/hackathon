import random

import pygame
import pygame_chart as pyc

from src import shared, utils

FAKE = [
    ("January", 100_000),
    ("February", 100_000),
    ("March", 120_000),
    ("April", 90_000),
    ("May", 100_000),
    ("June", 120_000),
    ("July", 150_000),
    ("August", 150_000),
    ("September", 160_000),
    ("October", 100_000),
    ("November", 120_000),
    ("December", 200_000),
]


class Income:
    def __init__(self) -> None:
        self.figure = pyc.Figure(shared.screen, 250, 50, 650, 600)

    def update(self):
        self.figure.line(
            "Income", [tup[0] for tup in FAKE], [tup[1] for tup in FAKE], "white"
        )

    def draw(self):
        self.figure.draw()
