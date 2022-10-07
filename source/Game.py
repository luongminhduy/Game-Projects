import pygame, sys
from pygame.locals import *
import time

from scenes.SceneManager import SceneManager
from utilities.constant import WHITE


##
# config: dictionary
#   {
#       width: num,
#       height: num,
#       fps: num,
#       scenes: list,
#       startScene: str,
#       windowCaption: str,
#       background: tuple
#   }
#

class Game:
    def __init__(self, config) -> None:
        self.config = config
        self.width = config["width"]
        self.height = config["height"]
        self.fps = config["fps"]
        self.scene = config["scene"]
        self.startScene = config["startScene"]
        self.windowCaption = config["windowCaption"]
        self.background = config["background"]
        self.clock = None
        # self.currentScene = None
        self.sceneManager = None
        self.screen = None

    def run(self):
        self.__setUp()
        lastFrameTime = time.time()

        while True:
            deltaTime = time.time() - lastFrameTime
            lastFrameTime = time.time()
            
            # print(deltaTime)
            self.__handleEvent()
            self.__update(deltaTime)
            self.__render()
            self.__endFrame()

            self.clock.tick(self.fps)

    def __handleEvent(self):
        pressedKeys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        self.sceneManager.getCurrentScene().processInput(events, pressedKeys)

    def __update(self, deltaTime):
        self.sceneManager.getCurrentScene().update(deltaTime)
        self.sceneManager.update()

    def __render(self):
        self.sceneManager.getCurrentScene().render()
        pygame.display.update()

    def __endFrame(self):
        self.sceneManager.getCurrentScene().screen.fill(WHITE)
        world = self.sceneManager.getCurrentScene().world
        if world:
            world.Step(1/self.fps, 10, 10)

    def __setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.windowCaption)
        self.clock = pygame.time.Clock()
        self.sceneManager = SceneManager()
        self.sceneManager.addScene([scene(self.screen, self.sceneManager) for scene in self.scene])
        self.sceneManager.setCurrentScene(self.startScene)
        self.screen.fill(self.background)
