import pygame
from scenes.BaseScene import BaseScene
from utilities.constant import *


class MenuScene(BaseScene):
    def __init__(self, screen: pygame.Surface, sceneManager) -> None:
        super().__init__("MenuScene", screen, sceneManager)
        self.__setUpScene()

    def __repr__(self) -> str:
        return '{self.__class__.__name__}()'.format(self=self)

    def processInput(self, events, pressedKeys):
        super().processInput(events, pressedKeys)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.sceneManager.startScene("GameScene")

    def update(self, deltaTime):
        pass

    def render(self):
        self.screen.blit(self.fieldImg, (0, 0))
        self.screen.blit(self.player1aSurf, (500, 400)) 

        self.screen.blit(self.titleSurf, self.titleRect)      

    def exit(self):
        print("exit MenuScene")

    def __setUpScene(self):
        self.titleFont = pygame.font.Font('freesansbold.ttf', 16)
        self.titleSurf = self.titleFont.render('Mini Football', True, GREEN)
        self.titleRect = self.titleSurf.get_rect()
        self.titleRect.center = (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.5)

        self.fieldImg = pygame.image.load("assets/images/field_with_brick.png")
        self.player1a = pygame.image.load("assets/images/player0.png")
        self.player1b = pygame.image.load("assets/images/player0.png")
        self.player2a = pygame.image.load("assets/images/player0.png")
        self.player2b = pygame.image.load("assets/images/player0.png")
        self.ball = pygame.image.load("assets/images/ball.png")
        
        self.player1aSurf = pygame.transform.scale(self.player1a, (50, 50))
        