
from abc import abstractmethod

import pygame


class AbstractBall:
    
    @abstractmethod
    def update(self, deltaTime):
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass