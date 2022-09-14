import pygame
from objects.BackGround import BackGround
pygame.init()
  
# CREATING CANVAS
canvas = pygame.display.set_mode((940, 528))
  
# TITLE OF CANVAS
pygame.display.set_caption("Zombie")
exit = False
#Load Image
bg = pygame.image.load("Zombie/assets/backGround.png")

#CREATE OBJECTS
backGround = BackGround(bg, 0, 0, 1)
#GAME LOOP  
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    backGround.display(canvas)        
    pygame.display.update()