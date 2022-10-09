
from abc import abstractmethod

import pygame


class AbstractScore:

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        pass