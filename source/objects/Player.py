import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)