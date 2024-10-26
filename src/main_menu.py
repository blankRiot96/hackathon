import pygame

from src import shared, utils


class Button:
    def __init__(self) -> None:
        pass


class MainMenu:
    def __init__(self) -> None:
        shared.next_state = None
        self.spark = utils.MetalExplosion()
        self.button = utils.ItalicButton(
            "Monkey",
            shared.srect.center,
            (140, 40),
        )

    def update(self):
        self.button.update()
        self.spark.check_mouse_spawn()
        self.spark.update()

    def draw(self):
        self.button.draw()
        self.spark.draw()
