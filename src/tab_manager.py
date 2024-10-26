import pygame

from src import shared, utils


class TabManager:
    BUTTONS_WIDTH = 150
    BUTTONS_HEIGHT = 40
    BUTTONS_PADDING = 10

    def __init__(self):
        self.tab_names = [
            "Inc",
            "Exp",
            "Sav",
        ]

        self.tabs = [
            utils.TabButton(
                name,
                (
                    30,
                    30 + (i * (TabManager.BUTTONS_HEIGHT + TabManager.BUTTONS_PADDING)),
                ),
                (TabManager.BUTTONS_WIDTH, TabManager.BUTTONS_HEIGHT),
            )
            for i, name in enumerate(self.tab_names)
        ]

    def update(self):
        for btn in self.tabs:
            btn.update()

    def draw(self):
        for btn in self.tabs:
            btn.draw()
