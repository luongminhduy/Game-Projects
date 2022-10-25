import pygame
from support import *
from config import *

class Coin(pygame.sprite.Sprite):
    collected_amount = 0
    current_player = None
    
    def __init__(self, pos) -> None:
        super().__init__()
        self.import_coin_asset()
        self.frame_idx = 0
        self.image = self.animation[self.frame_idx]
        self.rect = self.image.get_rect(topleft = pos)
        
    def import_coin_asset(self):
        asset_path = './assets/Coins'
        self.animation = []
        self.animation = import_full_asset(asset_path)
        
    def animate(self):
        self.frame_idx += animation_speed
        
        if self.frame_idx >= len(self.animation):
            self.frame_idx = 0
        
        self.image = self.animation[int(self.frame_idx)]        
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def check_collected(self):
        if self.rect.colliderect(Coin.current_player.rect):
            Coin.collected_amount += 1
            coin_fx.play()
            self.kill()
                   
    def update(self, x_shift):
        self.animate()
        self.check_collected()
        self.rect.x += x_shift # type: ignore
        
class Coins:
    def __init__(self, pos) -> None:
        self.coins = pygame.sprite.Group()
        
        for i in range(4):
            for j in range(3):
                coin = Coin((pos[0] + i * 15, pos[1] + j * 15))
                self.coins.add(coin)
                
    def update(self, x_shift):
        self.coins.update(x_shift)
