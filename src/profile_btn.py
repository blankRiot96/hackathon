import pygame

from src import shared, utils


class ProfileButton:
    def __init__(self) -> None:
        self.image = pygame.image.load("assets/profile.png").convert_alpha()
        self.image = self.image.subsurface(self.image.get_bounding_rect())
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect(
            topright=shared.srect.topright - pygame.Vector2(50, -50)
        )
        self.alpha = pygame.Vector2(255, 0)

    def update(self):
        hovering = self.rect.collidepoint(shared.mouse_pos)
        if hovering:
            self.alpha.move_towards_ip((150, 0), 20.5)
        else:
            self.alpha.move_towards_ip((255, 0), 20.5)

        self.image.set_alpha(self.alpha.x)

    def draw(self):
        shared.screen.blit(self.image, self.rect)
