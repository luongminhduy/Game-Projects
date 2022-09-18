import pygame
from objects.BackGround import BackGround
from objects.Hole import Hole
pygame.init()
  
# CREATING CANVAS
canvas = pygame.display.set_mode((940, 528))
  
# TITLE OF CANVAS
pygame.display.set_caption("Zombie")
exit = False

#Load Image
bgImg = pygame.image.load("assets/backGround.png")
holeImg = pygame.image.load("assets/hole.png")

#CREATE OBJECTS
backGround = BackGround(bgImg, 0, 0, 1)
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
hole = Hole(120, 120, matrix, 150, holeImg, (100, 100))

#GAME LOOP  
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    backGround.display(canvas)
    hole.display(canvas)        
    pygame.display.update()