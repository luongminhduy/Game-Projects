
from abc import abstractmethod

import pygame


class AbstractPlayer:

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass