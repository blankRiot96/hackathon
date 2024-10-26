import pygame
import pygame_gui

from src import shared, utils
from src.expenses import Expenses
from src.income import Income
from src.profile_btn import ProfileButton


class MainMenu:
    def __init__(self) -> None:
        shared.next_state = None
        self.manager = pygame_gui.UIManager(shared.srect.size)

        self.tabs = [
            pygame_gui.elements.UIButton(
                pygame.Rect(50, 50, 140, 40), "Income", self.manager
            ),
            pygame_gui.elements.UIButton(
                pygame.Rect(50, 100, 140, 40), "Expenses", self.manager
            ),
            pygame_gui.elements.UIButton(
                pygame.Rect(50, 150, 140, 40), "Savings", self.manager
            ),
        ]

        self.profile = ProfileButton()
        self.current = None

    def update(self):
        self.manager.update(shared.dt)
        self.profile.update()

        for event in shared.events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.tabs[0]:
                    self.current = Income()
                elif event.ui_element == self.tabs[1]:
                    self.current = Expenses()

        if self.current is not None:
            self.current.update()

    def draw(self):
        self.manager.draw_ui(shared.screen)
        self.profile.draw()

        if self.current is not None:
            self.current.draw()
