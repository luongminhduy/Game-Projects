import pygame
import sys
from config import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(level_map, screen)
bg = pygame.image.load("./assets/BackGround.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    screen.blit(bg, bg.get_rect())
    level.run()
    
    pygame.display.update()
    clock.tick(60)