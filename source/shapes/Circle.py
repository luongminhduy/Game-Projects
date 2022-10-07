
from typing import Literal
import pygame
from shapes.Shape import Shape


class Circle(Shape):
    def __init__(self) -> None:
        self.center = pygame.math.Vector2(0, 0)
        self.radius = 0

    def isInsideShape(self, coor: tuple[Literal[0], Literal[0]]) -> bool:
        return False

    def synWithBody(self, position: pygame.math.Vector2, image: pygame.Surface):
        self.center.x = position.x + image.get_width() * 0.5
        self.center.y = position.y + image.get_height() * 0.5
        
        if self.radius == 0:
            self.radius = image.get_width() * 0.5