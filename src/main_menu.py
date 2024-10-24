import pygame

from src import shared, utils


class Button:
    def __init__(self) -> None:
        pass


class MainMenu:
    def __init__(self) -> None:
        self.spark = utils.MetalExplosion()

    def update(self):
        self.spark.check_mouse_spawn()
        self.spark.update()

    def draw(self):
        self.spark.draw()
