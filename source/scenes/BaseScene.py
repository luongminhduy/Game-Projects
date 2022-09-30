import pygame

from scenes.SceneManager import SceneManager


class BaseScene:
    def __init__(self, key: str, screen: pygame.Surface, sceneManager: SceneManager) -> None:
        self.key = key
        self.screen: pygame.Surface = screen
        self.sceneManager = sceneManager
        self.events = None

    def processInput(self, events, pressedKeys):
        self.events = events

    def update(self, deltaTime):
        pass

    def render(self):
        pass

    def exit(self):
        pass