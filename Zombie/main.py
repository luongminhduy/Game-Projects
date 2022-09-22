from tracemalloc import start
import pygame
from pygame import mixer
#from Zombie.objects.Hammer import Hammer
from objects.BackGround import BackGround
from objects.Hole import Hole
from objects.Hammer import Hammer

pygame.init()
mixer.init()
# CREATING CANVAS
canvas = pygame.display.set_mode((940, 528))
  
# TITLE OF CANVAS
pygame.display.set_caption("Zombie")
exit = False

#Load Image
bgImg = pygame.image.load("./Zombie/assets/backGround.png")
holeImg = pygame.image.load("./Zombie/assets/hole.png")
hammerImg = pygame.image.load("./Zombie/assets/hammer_3.png")

#Load Audio
hit = pygame.mixer.Sound("./Zombie/assets/audio/hit.wav")
music = pygame.mixer.Sound("./Zombie/assets/audio/music.mp3")
music.set_volume(0.3)
#CREATE OBJECTS
backGround = BackGround(bgImg, 0, 0, 1)
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
hole = Hole(120, 120, matrix, 150, holeImg, (100, 100))
hammer = Hammer(hammerImg, 10, hit)

pygame.mouse.set_visible(False)
pygame.mixer.Sound.play(music, -1)
#GAME LOOP
startTick = 0
endTick = 0  
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN and hammer.attack == False:
            startTick = pygame.time.get_ticks()
            hammer.hit(0, 0)
            hammer.changeAnimation()
    endTick = pygame.time.get_ticks()
    if (startTick != 0 and endTick - startTick >= 100):
        startTick = 0
        endTick = 0
        hammer.unHit()
        hammer.changeAnimation()
    backGround.display(canvas)
    hole.display(canvas)
    hammer.display(canvas)       
    pygame.display.update()