import pygame
from scenes.BaseScene import BaseScene
from utilities.constant import *
from pygame import mixer

class MenuScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("MenuScene", screen, sceneManager)
        self.__load()

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.button.get_rect(topleft = (WINDOW_WIDTH * 0.35, WINDOW_HEIGHT * 0.4)).collidepoint(x, y):
                    self.sceneManager.startScene("GameScene")

    def start(self):
        pass

    def update(self, deltaTime):
        pass

    def render(self):
        self.screen.blit(self.firstimage, (-500, 0))  
        self.screen.blit(self.button, (WINDOW_WIDTH * 0.35, WINDOW_HEIGHT * 0.4))      

    def exit(self):
        print("exit MenuScene")

    def __load(self):
        self.button = pygame.image.load("assets/images/button.png")
        self.firstimage = pygame.image.load("assets/images/first.png")
        theme = mixer.Sound("assets/sounds/theme.wav")
        theme.set_volume(0.3)
        mixer.Sound.play(theme, -1)

        
        