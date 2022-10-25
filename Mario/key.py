import pygame
from support import *

class Key(pygame.sprite.Sprite):
    collected_amount = 0
    
    def __init__(self, pos) -> None:
        super().__init__()
        self.frame_idx = 0
        self.image = pygame.image.load('./assets/key.png')       
        self.image = pygame.transform.scale(self.image, (self.image.get_width() / 7, self.image.get_height() / 7))
        self.rect = self.image.get_rect(topleft = pos)
        
    def check_collected(self, sprite):
        if self.rect.colliderect(sprite.rect):
            Key.collected_amount += 1
            coin_fx.play()
            self.kill()
            
    def update(self, x_shift, sprite):
        self.check_collected(sprite)
        self.rect.x += x_shift # type: ignore