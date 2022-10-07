import pygame
from scenes.BaseScene import BaseScene
from utilities.constant import *


class MenuScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("MenuScene", screen, sceneManager)
        self.__load()

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.sceneManager.startScene("GameScene")

    def start(self):
        pass

    def update(self, deltaTime):
        pass

    def render(self):
        self.screen.blit(self.titleSurf, self.titleRect)      

    def exit(self):
        print("exit MenuScene")

    def __load(self):
        self.titleFont = pygame.font.Font('freesansbold.ttf', 32)
        self.titleSurf = self.titleFont.render('Mini Football, press 0 to change scene!', True, GREEN)
        self.titleRect = self.titleSurf.get_rect()
        self.titleRect.center = (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.5)

        
        