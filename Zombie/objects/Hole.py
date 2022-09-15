from mimetypes import init
from turtle import distance
import pygame

class Hole:
    def __init__(self, x, y, matrix, distance, sprite, size) -> None:
        self.x = x
        self.y = y
        self.matrix = matrix
        self.distance = distance
        self.sprite = sprite
        self.size = size

    def display(self, screen: pygame.Surface) ->None:
        i = 0
        j = 0
        for row in self.matrix:
            for hole in row:
                screen.blit(pygame.transform.scale(self.sprite, self.size),
                (self.x + 2 * i * self.distance, self.y + j * self.distance))
                i = i + 1
            i = 0    
            j = j + 1    