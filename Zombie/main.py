import random
from secrets import choice
from tracemalloc import start
import pygame
from pygame import mixer
#from Zombie.objects.Hammer import Hammer
from objects.BackGround import BackGround
from objects.Hole import Hole
from objects.Hammer import Hammer
from objects.Mole import *

pygame.init()
mixer.init()
# CREATING CANVAS
canvas = pygame.display.set_mode((940, 528))
  
# TITLE OF CANVAS
pygame.display.set_caption("Whack a mole")
exit = False

#Load Image
bgImg = pygame.image.load("assets/backGround.png")
holeImg = pygame.image.load("assets/hole.png")
hammerImg = pygame.image.load("assets/hammer_3.png")

#Load Audio
hit = pygame.mixer.Sound("assets/audio/hit.wav")
music = pygame.mixer.Sound("assets/audio/music.mp3")
music.set_volume(0.3)
#CREATE OBJECTS
backGround = BackGround(bgImg, 0, 0, 1)
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
hole = Hole(120, 120, matrix, 150, holeImg, (100, 100))
hammer = Hammer(hammerImg, 10, hit)

moles = []
i = 0
j = 0
for row in matrix:
    for mole in row:
        moles.append(Mole(120 + 2 * i * 150 + 10, 120 + j * 150 - 42, MoleAnimation.NONE))
        i = i + 1
    i = 0    
    j = j + 1 

moles[random.choice(list(range(len(moles))))].animation = MoleAnimation.UP

pygame.mouse.set_visible(False)
pygame.mixer.Sound.play(music, -1)

#GAME LOOP
startTick = 0
endTick = 0  

startMoleTick = pygame.time.get_ticks()
endMoleTick = startMoleTick

while not exit:
    
    
    endMoleTick = pygame.time.get_ticks()
    if endMoleTick - startMoleTick > 700:
        current_mole_up = []
    
        for i in range(len(moles)):
            if moles[i].animation != MoleAnimation.NONE:
                current_mole_up.append(i)
            
        if len(current_mole_up) <= 3:
            new_up = random.choice(list(range(len(moles))))           
            
            if new_up not in current_mole_up:
                moles[new_up].animation = MoleAnimation.UP
                current_mole_up.append(new_up)
                
        startMoleTick = endMoleTick
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
            
        if event.type == pygame.MOUSEBUTTONDOWN and hammer.attack == False:
            startTick = pygame.time.get_ticks()
            hammer.hit(0, 0)
            hammer.changeAnimation()
            
            current_mole_up = []
            
            for i in range(len(moles)):
                if moles[i].animation != MoleAnimation.NONE and moles[i].animation != MoleAnimation.DIE:
                    current_mole_up.append(i)
                    
            pos = pygame.mouse.get_pos()

            for moleIdx in current_mole_up:
                if moles[moleIdx].rect_surround != None and moles[moleIdx].rect_surround.collidepoint(pos):
                    moles[moleIdx].animation = MoleAnimation.DIE

                    print(current_mole_up)
                    print("score: ",Mole.death," pos: ", moleIdx)
                    print("--------------------------------------------------------")
                    print("miss: ",Mole.alive)
                    print("--------------------------------------------------------")
            
            
            
    endTick = pygame.time.get_ticks()
    
    if (startTick != 0 and endTick - startTick >= 100):
        startTick = 0
        endTick = 0
        hammer.unHit()
        hammer.changeAnimation()
        
    backGround.display(canvas)
    hole.display(canvas)
    for mole in moles:
        mole.display(canvas)   
    hammer.display(canvas)
           
    pygame.display.update()