import pygame
from config import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.import_player_asset()
        self.frame_idx = 0
        self.status = 'idle'
        self.animation_speed = animation_speed
        self.image = self.animations[self.status][self.frame_idx]
        self.rect = self.image.get_rect(topleft = pos)
        self.right_moving = True
        self.wearing_cuirass = False
                       
        #player movement
        self.speed = player_speed
        self.direction = pygame.Vector2((0,0))
        self.gravity = player_gravity
        self.jump_speed = player_jump_speed
        self.touch_ground = True
        self.touch_ceiling = False
        self.touch_left = False
        self.touch_right = False
        
        #player unlock chest
        self.using_key = False

    def import_player_asset(self):
        asset_path = './assets/Player/'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[], 'shoot':[], 'melee':[], 'slide':[], 'dead':[]}
        
        for animation in self.animations.keys():
            full_path = asset_path + animation
            
            if animation == 'idle':
                x, y, width, height  = 110, 20, 340, 520
            elif animation == 'run':
                x, y, width, height  = 110, 20, 440, 520
            elif animation in ['jump', 'fall']:
                x, y, width, height  = 110, 20, 400, 520
            elif animation in ['shoot', 'melee', 'dead']:
                x, y, width, height  = 110, 20, 470, 520
            else:
                x, y, width, height  = 50, 20, 470, 520
                
            self.animations[animation] = import_folder(full_path, x, y, width, height)
        
        super_asset_path = './assets/SuperPlayer/'
        self.super_animations = {'idle':[], 'run':[], 'jump':[], 'fall':[], 'attack':[], 'dead':[]}
        
        for animation in self.super_animations.keys():
            full_path = super_asset_path + animation
            
            if animation in ['idle', 'run', 'jump', 'fall']:
                x, y, width, height  = 15, 20, 490, 650
            elif animation == 'attack':
                x, y, width, height  = 15, 20, 540, 650
            else:
                x, y, width, height  = 10, 20, 900, 650
                
            self.super_animations[animation] = import_folder(full_path, x, y, width, height, 11)
            
    def animate(self):
        
        if self.wearing_cuirass:
            animation = self.super_animations[self.status]
        else:
            animation = self.animations[self.status]
        
        self.frame_idx += self.animation_speed
        if self.frame_idx >= len(animation):
            self.frame_idx = 0
            
        image = animation[int(self.frame_idx)]
        
        if self.right_moving:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
        
        # Change the rect    
        self.rect = self.image.get_rect(center = self.rect.center)
        if self.touch_ground and self.touch_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.touch_ground and self.touch_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.touch_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.touch_ceiling and self.touch_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.touch_ceiling and self.touch_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.touch_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        # else: 
        #     self.rect = self.image.get_rect(center = self.rect.center)
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_k]:
            self.using_key = True
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.right_moving = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.right_moving = False
        else: 
            self.direction.x = 0
            
        if keys[pygame.K_UP] and self.touch_ground:
            jump_fx.play()
            self.jump()
            
    def get_status(self):
        if self.direction.y > self.gravity:
            self.status = 'fall'
        elif self.direction.y < 0:
            self.status = 'jump'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'                             
            
    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        if (self.touch_ground):
            self.direction.y = player_jump_speed
            self.touch_ground = False