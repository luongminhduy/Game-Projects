from typing import Literal
import pygame

from interface.AbstractBall import AbstractBall

class Ball(AbstractBall):
    def __init__(self, image: pygame.Surface, position: tuple[Literal[0], Literal[0]]) -> None:
        super().__init__()
        self.image = image
        self.position = pygame.math.Vector2(position)
        self.radius = 16

        self.__adjustImage()
        self.body = None
        self.fixture = None

    def update(self, deltaTime):
        self.position.x = self.body.position.x
        self.position.y = self.body.position.y
        
    def getX(self):
        return self.body.position.x
    
    def getY(self):
        return self.body.position.y
    
    def setPostion(self, position: tuple[Literal[0], Literal[0]]):
        self.position = self.body.position = pygame.math.Vector2(position)
        
    def render(self, screen: pygame.Surface):
        screen.blit(self.image, (self.position.x, self.position.y))

    def __adjustImage(self):
        self.image = pygame.transform.scale(self.image, (2 * self.radius, 2 * self.radius))