
from abc import abstractmethod
from typing import Literal

import pygame



class Shape:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def isInsideShape(self, coor: tuple[Literal[0], Literal[0]]) -> bool:
        pass

    @abstractmethod
    def synWithBody(self, position, image: pygame.Surface):
        pass