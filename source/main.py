
from scenes.MenuScene import MenuScene
from scenes.GameScene import GameScene
from Game import Game
from utilities.constant import *

config  = {
    "width": WINDOW_WIDTH,
    "height": WINDOW_HEIGHT,
    "fps": FPS,
    "scene": [MenuScene, GameScene],
    "startScene": "MenuScene",
    "windowCaption": "Mini Football",
    "background": WHITE
}

if __name__ == '__main__':
    game = Game(config)
    game.run()