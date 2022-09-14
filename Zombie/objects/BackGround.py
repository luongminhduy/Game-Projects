from ast import Num
from tokenize import Number
import pygame

class BackGround:
   def __init__(self, sprite, x, y, size) -> None:
    self.sprite = sprite
    self.x = x
    self.y = y
    self.size = size
  
   def display(self, screen:  pygame.Surface)->None:
    screen.blit(self.sprite, (self.x, self.y))
   

