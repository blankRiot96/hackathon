import random

import pygame
import pygame_chart as pyc

from src import shared, utils

FAKE = [
    ("January", random.randint(50_000, 70_000)),
    ("February", random.randint(50_000, 200_000)),
    ("March", random.randint(10_000, 200_000)),
    ("April", random.randint(50_000, 170_000)),
    ("May", random.randint(100_000, 150_000)),
    ("June", random.randint(70_000, 200_000)),
    ("July", random.randint(70_000, 200_000)),
    ("August", random.randint(100_000, 200_000)),
    ("September", random.randint(100_000, 200_000)),
    ("October", random.randint(50_000, 90_000)),
    ("November", random.randint(50_000, 100_000)),
    ("December", random.randint(50_000, 100_000)),
]


FAKE = [(month, expense * 0.7) for month, expense in FAKE]


class Expenses:
    def __init__(self) -> None:
        self.figure = pyc.Figure(shared.screen, 250, 50, 650, 600)

    def update(self):
        self.figure.line(
            "Expenses", [tup[0] for tup in FAKE], [tup[1] for tup in FAKE], "white"
        )

    def draw(self):
        self.figure.draw()
