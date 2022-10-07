
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
        self.active = False
        self.flipX = False
        self.activeRadius = 30

        self.__adjustImage()
        self.body = None
        self.fixture = None

    def update(self, deltaTime):
        self.position.x = self.body.position.x - 10
        self.position.y = self.body.position.y - 10 

    
        # angle = math.atan2(self.body.linearVelocity.y, self.body.linearVelocity.x)
        # # self.body.setTransform(self.body.getWorldCenter(), angle - math.pi / 2)
        # print((angle - math.pi / 2) * (180 / math.pi))
        
        # self.image = pygame.transform.rotate(self.image, (angle) * (180 / math.pi))

    def render(self, screen: pygame.Surface):
        if self.active:
            screen.blit(self.circleImage, (self.position.x, self.position.y))
        
        screen.blit(self.image, (self.position.x + 5, self.position.y + 5))

    def flip(self, flipX: bool, flipY: bool):
        if flipX and not self.flipX:
            self.flipX = flipX
            self.image = pygame.transform.flip(self.image, flipX, flipY)

        if not flipX and self.flipX:
            self.flipX = flipX
            self.image = pygame.transform.flip(self.image, flipX, flipY)

    # def __rotate(self):
    #     self.image = pygame.transform.rotate(self.image, self.degree)
    #     self.degree = 0

    def __adjustImage(self):
        self.image = self.image.convert()
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.image = pygame.transform.scale(self.image, (2 * self.radius, 2 * self.radius))

        self.circleImage = self.circleImage.convert()
        self.circleImage.set_colorkey(self.circleImage.get_at((0, 0)), pygame.RLEACCEL)
        self.circleImage = pygame.transform.scale(self.circleImage, (2 * self.activeRadius, 2 * self.activeRadius))
