import pygame
from support import *

class Cuirass(pygame.sprite.Sprite):
    collected_amount = 0
    
    def __init__(self, pos) -> None:
        super().__init__()
        self.frame_idx = 0
        self.image = pygame.image.load('./assets/cuirass.png')       
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 7, self.image.get_height() / 7))
        self.rect = self.image.get_rect(midbottom = pos)
        self.stop_y = self.rect.centery - 40
        
        
    def check_collected(self, sprite):
        if self.rect.colliderect(sprite.rect):
            if sprite.wearing_cuirass:
                Cuirass.collected_amount += 1
            else:
                transform_fx.play()
                sprite.wearing_cuirass = True
                
            self.kill()
            
    def animate(self):
        if self.rect.centery <= self.stop_y:
            return
        
        self.rect.y -= animation_speed
            
    def update(self, x_shift, sprite):
        self.check_collected(sprite)
        self.animate()
        self.rect.x += x_shift # type: ignore