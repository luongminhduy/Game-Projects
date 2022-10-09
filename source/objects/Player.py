
from typing import Literal
import pygame

from interface.AbstractPlayer import AbstractPlayer


class Player(AbstractPlayer):

    def __init__(self, image: pygame.Surface, circleImage: pygame.Surface, position: tuple[Literal[0], Literal[0]]) -> None:
        super().__init__()
        self.image = image
        self.circleImage = circleImage
        self.sprite = None
        self.position = pygame.math.Vector2(position)
        self.radius = 25
        self.degree = 0
        self.flipX = -1
        self.flipY = None
        self.active = False
        self.activeRadius = 30

        self.__adjustImage()
        self.body = None
        self.fixture = None

    def update(self, deltaTime):
        self.position.x = self.body.position.x - 10
        self.position.y = self.body.position.y - 10
   
    def setPosition(self, position: tuple[Literal[0], Literal[0]]):
        self.position = self.body.position = pygame.math.Vector2(position)
            
    def render(self, screen: pygame.Surface):
        if self.active:
            screen.blit(self.circleImage, (self.position.x, self.position.y))
        screen.blit(self.image, (self.position.x + 5, self.position.y + 5))

    def flip(self, flipX: int, flipY: int):
        if flipX is None and self.flipY != flipY:
            if self.flipY and self.flipY * -1 == flipY:
                self.image = pygame.transform.rotate(self.image, 180)
            else: self.image = pygame.transform.rotate(self.image, flipY * self.flipX * -90)
        elif flipY is None and self.flipX != flipX:
            if self.flipX and self.flipX * -1 == flipX:
                self.image = pygame.transform.flip(self.image, True, False)
            else: self.image = pygame.transform.rotate(self.image, flipX * self.flipY * 90)
        self.flipX = flipX
        self.flipY = flipY

    def __adjustImage(self):
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.image = pygame.transform.scale(self.image, (2 * self.radius, 2 * self.radius))

        self.circleImage = self.circleImage.convert()
        self.circleImage.set_colorkey(self.circleImage.get_at((0, 0)), pygame.RLEACCEL)
        self.circleImage = pygame.transform.scale(self.circleImage, (2 * self.activeRadius, 2 * self.activeRadius))
