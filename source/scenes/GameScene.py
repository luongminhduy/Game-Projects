import pygame
from scenes.BaseScene import BaseScene


class GameScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("GameScene", screen, sceneManager)

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.sceneManager.startScene("MenuScene")

    def update(self, deltaTime):
        self.screen.fill((0,0,0))

    def render(self):
        pass
        
    def exit(self):
        print("exit GameScene")