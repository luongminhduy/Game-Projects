from typing import Literal
import pygame
from utilities.constant import WHITE, BLACK
from datetime import timedelta
from interface.AbstractScore import AbstractScore

class Score(AbstractScore):
    def __init__(self, image: pygame.Surface, position: tuple[Literal[0], Literal[0]]) -> None:
        super().__init__()
        self.image = image
        self.position = pygame.math.Vector2(position)
        self.body = None

    def update(self):
        pass
    
    def render(self, screen: pygame.Surface, redScore: int, blueScore: int, timelimit: int):
        screen.blit(self.image, (self.position.x, self.position.y))
        self.titleFont = pygame.font.Font('freesansbold.ttf', 30)
        self.titleSurf = self.titleFont.render(str(redScore) + '   ' + str(blueScore), True, WHITE)
        self.titleRect = self.titleSurf.get_rect()
        self.titleRect.center = (self.position.x + 177, self.position.y + 20)
        screen.blit(self.titleSurf, self.titleRect)
        timeSurf = self.titleFont.render(str(timedelta(seconds= timelimit)), True, BLACK)
        timeRect = timeSurf.get_rect()
        timeRect.center = (self.position.x - 150, self.position.y + 20)
        screen.blit(timeSurf, timeRect)