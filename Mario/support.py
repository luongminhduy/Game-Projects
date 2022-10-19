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