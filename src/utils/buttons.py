import typing as t

import pygame

from src import shared

from .load import load_font


class ItalicButton:
    TEXT_COLOR = (193, 184, 163)
    BACKGROUND_COLOR = "purple"
    HOVER_COLOR = "brown"

    def __init__(self, text: str, center: t.Sequence, size: tuple[int, int]) -> None:
        self.font = load_font("assets/fonts/bold1.ttf", 24)
        self.text = text
        self.center = pygame.Vector2(center)
        self.base_surf = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(
            self.base_surf,
            self.BACKGROUND_COLOR,
            (0, 0, *size),
            border_top_right_radius=10,
            border_bottom_left_radius=10,
        )

        self.hover_surf = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(
            self.hover_surf,
            self.HOVER_COLOR,
            (0, 0, *size),
            border_top_right_radius=10,
            border_bottom_left_radius=10,
        )

        self.outline_surf = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(
            self.outline_surf,
            "white",
            (0, 0, *size),
            border_top_right_radius=10,
            border_bottom_left_radius=10,
            width=3,
        )

        self.rect = self.base_surf.get_rect(center=self.center)

        self.surf = self.base_surf
        self.text_surf = self.font.render(self.text, True, self.TEXT_COLOR)
        self.text_rect = self.text_surf.get_rect(center=self.center)
        self.clicked = False

    def update(self):
        self.clicked = False

        clicked = False
        for event in shared.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

        if self.rect.collidepoint(shared.mouse_pos):
            self.surf = self.hover_surf
            if clicked:
                self.clicked = True
        else:
            self.surf = self.base_surf

    def draw(self):
        shared.screen.blit(self.surf, self.rect)
        shared.screen.blit(self.outline_surf, self.rect)
        shared.screen.blit(self.text_surf, self.text_rect)
