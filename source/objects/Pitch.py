from typing import Literal
import pygame

from interface.AbstractPitch import AbstractPitch
from physics.Body import Body
from shapes.Rectangle import Rectangle

class Pitch(AbstractPitch):
    def __init__(self, image: pygame.Surface, position: tuple[Literal[0], Literal[0]]) -> None:
        super().__init__()
        self.image = image
        self.position = pygame.math.Vector2(position)
        self.body = None

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        screen.blit(self.image, (self.position.x, self.position.y))