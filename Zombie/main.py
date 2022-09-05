import pygame
  
pygame.init()
  
# CREATING CANVAS
canvas = pygame.display.set_mode((1000, 600))
  
# TITLE OF CANVAS
pygame.display.set_caption("Zombie")
exit = False

#CREATE OBJECTS

#GAME LOOP  
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()