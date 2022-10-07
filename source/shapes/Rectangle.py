
from typing import Literal
import pygame
from shapes.Shape import Shape


class Rectangle(Shape):
    def __init__(self) -> None:
        self.min = pygame.math.Vector2(0, 0)
        self.max = pygame.math.Vector2(0, 0)

    def isInsideShape(self, coor: tuple[Literal[0], Literal[0]]) -> bool:
        return False

    def synWithBody(self, position: pygame.math.Vector2, image: pygame.Surface):
        self.min.x = position.x
        self.min.y = position.y + image.get_height()
        self.max.x = position.x + image.get_width()
        self.max.y = position.y
