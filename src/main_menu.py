import pygame

from src import shared


class Button:
    pass


class MainMenu:
    def update(self):
        pass

    def draw(self):
        shared.screen.fill(
            "blue",
            rect=pygame.Rect(
                0,
                0,
                shared.srect.width / 2,
                shared.srect.height,
            ),
        )
        shared.screen.fill(
            "red",
            rect=pygame.Rect(
                shared.srect.width / 2,
                0,
                shared.srect.width / 2,
                shared.srect.height,
            ),
        )
