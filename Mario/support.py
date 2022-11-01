import os
import pygame
from config import *

def import_folder(path, x, y, width, height, scale_number = 10):
    surfaces = []
    
    for _,_,file_names in os.walk(path):
        for file_name in file_names:
            full_path = path + '/' + file_name            
            surfaces.append(pygame.transform.scale(pygame.image.load(full_path).convert_alpha().subsurface((x, y, width, height)), (width/scale_number, height/scale_number)))
            
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
jump_fx.set_volume(1)

game_over_fx = pygame.mixer.Sound('sounds/GameOver.wav')
game_over_fx.set_volume(1)

melee_fx = pygame.mixer.Sound('sounds/UsingKnife.wav')
melee_fx.set_volume(1)

shoot_fx = pygame.mixer.Sound('sounds/Shoot.wav')
shoot_fx.set_volume(1)

hurt_fx = pygame.mixer.Sound('sounds/Hurt.wav')
hurt_fx.set_volume(1)

coin_fx = pygame.mixer.Sound('sounds/coin.wav')
coin_fx.set_volume(1)

unlocking_fx = pygame.mixer.Sound('sounds/unlocking.wav')
unlocking_fx.set_volume(1)

transform_fx = pygame.mixer.Sound('sounds/transform.flac')
transform_fx.set_volume(1)

enemyAttack_fx = pygame.mixer.Sound('sounds/EnemyAttack.wav')
enemyAttack_fx.set_volume(1)

win_fx = pygame.mixer.Sound('sounds/win.wav')
win_fx.set_volume(1)