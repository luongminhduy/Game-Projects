import pygame
from cuirass import Cuirass
from support import *
from config import *

class Chest(pygame.sprite.Sprite):
    
    def __init__(self, pos) -> None:
        super().__init__()
        self.import_chest_asset()
        self.frame_idx = 0
        self.image = self.animation[self.frame_idx]
        self.rect = self.image.get_rect(bottomleft = pos)
        self.is_blocked = True
        self.item = None
        
    def import_chest_asset(self):
        asset_path = './assets/Chest'
        self.animation = []
        self.animation = import_full_asset(asset_path, 6)
        
    def animate(self):
        if self.is_blocked or self.frame_idx == len(self.animation) - 1: return                
   
        self.frame_idx += animation_speed
        
        if self.frame_idx >= len(self.animation):
            self.item = pygame.sprite.GroupSingle()
            self.item.add(Cuirass(self.rect.center))
            
            self.frame_idx = len(self.animation) - 1
        
        self.image = self.animation[int(self.frame_idx)]        
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def unlock(self):
        self.is_blocked = False
        self.frame_idx = 1
        unlocking_fx.play()
              
    def update(self, x_shift, display_surface, sprite):          
        self.animate()
        
        if self.item != None:
            self.item.update(x_shift, sprite)
            self.item.draw(display_surface)
            
        self.rect.x += x_shift # type: ignore