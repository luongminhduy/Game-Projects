import os
import pygame
from config import *

def import_folder(path, x, y, width, height):
    surfaces = []
    
    for _,_,file_names in os.walk(path):
        for file_name in file_names:
            full_path = path + '/' + file_name            
            surfaces.append(pygame.transform.scale(pygame.image.load(full_path).convert_alpha().subsurface((x, y, width, height)), (width/10, height/10)))
            
    return surfaces

def import_full_asset(path, scale_number = 10):
    surfaces = []
    
    for _,_,file_names in os.walk(path):
        for file_name in file_names:
            full_path = path + '/' + file_name
            asset = pygame.image.load(full_path)          
            surfaces.append(pygame.transform.scale(asset, (asset.get_width() / scale_number, asset.get_height() / scale_number)))
            
    return surfaces

#game sound
pygame.mixer.pre_init()
pygame.mixer.init()

jump_fx = pygame.mixer.Sound('sounds/jump.wav')
jump_fx.set_volume(0.5)

game_over_fx = pygame.mixer.Sound('sounds/GameOver.wav')
game_over_fx.set_volume(0.5)

melee_fx = pygame.mixer.Sound('sounds/UsingKnife.wav')
melee_fx.set_volume(0.5)

shoot_fx = pygame.mixer.Sound('sounds/Shoot.wav')
shoot_fx.set_volume(0.5)

hurt_fx = pygame.mixer.Sound('sounds/Hurt.wav')
hurt_fx.set_volume(0.5)

coin_fx = pygame.mixer.Sound('sounds/coin.wav')
coin_fx.set_volume(0.5)

unlocking_fx = pygame.mixer.Sound('sounds/unlocking.wav')
unlocking_fx.set_volume(1)