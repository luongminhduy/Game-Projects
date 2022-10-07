from abc import abstractmethod
import pygame

from scenes.SceneManager import SceneManager


class BaseScene:
    def __init__(self, key: str, screen: pygame.Surface, sceneManager: SceneManager) -> None:
        self.key = key
        self.screen: pygame.Surface = screen
        self.sceneManager = sceneManager
        self.events = None
        self.world = None

    def processInput(self, events, pressedKeys):
        self.events = events
        self.pressedKeys = pressedKeys

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self, deltaTime):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def exit(self):
        pass