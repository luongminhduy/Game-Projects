import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = pos)        
        
        #player movement
        self.speed = player_speed
        self.direction = pygame.Vector2((0,0))
        self.gravity = player_gravity
        self.jump_speed = player_jump_speed
        self.canJump = True
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else: 
            self.direction.x = 0
            
        if keys[pygame.K_UP] and self.canJump:
            self.jump()
            
    def update(self):
        self.get_input()
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = player_jump_speed
        self.canJump = False