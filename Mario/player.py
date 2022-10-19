import pygame
from config import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.import_player_asset()
        self.frame_idx = 0
        self.animation_speed = animation_speed
        self.image = self.animations['idle'][self.frame_idx]
        self.rect = self.image.get_rect(topleft = pos)        
        
        #player movement
        self.speed = player_speed
        self.direction = pygame.Vector2((0,0))
        self.gravity = player_gravity
        self.jump_speed = player_jump_speed
        self.canJump = True

    def import_player_asset(self):
        asset_path = './assets/Player/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[], 'shoot':[], 'melee':[], 'slide':[], 'dead':[]}
        
        for animation in self.animations.keys():
            full_path = asset_path + animation
            
            if animation == 'idle':
                x, y, width, height  = 110, 20, 340, 520
            elif animation == 'run':
                x, y, width, height  = 110, 20, 440, 520
            elif animation == 'jump':
                x, y, width, height  = 110, 20, 400, 520
            elif animation == 'fall':
                x, y, width, height  = 110, 20, 400, 520
            elif animation == 'shoot':
                x, y, width, height  = 110, 20, 470, 520
            elif animation == 'melee':
                x, y, width, height  = 110, 20, 470, 520
            elif animation == 'slide':
                x, y, width, height  = 50, 20, 470, 520
            else:
                x, y, width, height  = 110, 20, 470, 520
                
            self.animations[animation] = import_folder(full_path, x, y, width, height)
            
    def animate(self):
        animation = self.animations['slide']
        
        self.frame_idx += self.animation_speed
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
            
        self.image = animation[int(self.frame_idx)]
        
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
        self.animate()
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = player_jump_speed
        self.canJump = False