import pygame
import sys
from config import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(level_map, screen)
bg = pygame.image.load("./assets/BackGround.jpg")
color = (255,0, 0)
#---
res = (screen_width, screen_height) 
  
screen = pygame.display.set_mode(res) 
  

color = (255,255,255) 
  

color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() - 150 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() - 150 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('play' , True , color)
quitText = smallfont.render('quit', True, color)
aboutText = smallfont.render('about', True, color)
howToPlay = smallfont.render('nhay len dau de tieu diet ke dich, tim chia khoa de mo ruong lay ao giap tang mang', True, color_dark)
gameOver = smallfont.render('Game Over', True, color_dark)
newGame = smallfont.render('New Game', True, color)
level.running = "menu" 
  
while True: 
  if (level.running == "menu"):  
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                #pygame.quit()
                level.running = "playing"
            elif width/2 <= mouse[0] <= width/2+140 and height/2 + 100 <= mouse[1] <= height/2+140:
                pygame.quit()
            elif width/2 <= mouse[0] <= width/2+140 and height/2 + 200 <= mouse[1] <= height/2+240:  
                level.running = "about"  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
    screen.blit(bg, bg.get_rect())  
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])       
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])

    if width/2 <= mouse[0] <= width/2+140 and height/2 + 100 <= mouse[1] <= height/2+140:
        pygame.draw.rect(screen,color_light,[width/2,height/2 + 100,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2 + 100,140,40])

    if width/2 <= mouse[0] <= width/2+140 and height/2 + 200 <= mouse[1] <= height/2+240:
        pygame.draw.rect(screen,color_light,[width/2,height/2 + 200,140,40])
    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2 + 200,140,40])
    

    # superimposing the text onto our button 
    screen.blit(text, (width/2+50,height/2))
    screen.blit(quitText, (width/2 + 50, height/2 + 100))
    screen.blit(aboutText, (width/2 + 30, height/2 + 200))  
      
    # updates the frames of the game 
    pygame.display.update()
  elif level.running == 'about':
    screen.fill((60,25,60))
    screen.blit(bg, bg.get_rect())
    for ev in pygame.event.get():        
        if ev.type == pygame.QUIT: 
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2+200 <= mouse[1] <= height/2+240: 
                #pygame.quit()
                level.running = "playing"
    mouse = pygame.mouse.get_pos()
    if width/2 <= mouse[0] <= width/2+140 and height/2+200 <= mouse[1] <= height/2+240: 
        pygame.draw.rect(screen,color_light,[width/2,height/2 + 200,140,40])       
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2 + 200,140,40])           
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    screen.blit(text, (width/2+50,height/2 + 200))
    screen.blit(howToPlay, (20, 100))
    pygame.display.update()
  elif level.running == 'gameover':
    screen.fill((60,25,60))
    screen.blit(bg, bg.get_rect())
    for ev in pygame.event.get():        
        if ev.type == pygame.QUIT: 
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                #pygame.quit()
                level.running = "playing"
    mouse = pygame.mouse.get_pos()
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,160,40])       
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,160,40])           
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    screen.blit(newGame, (width/2,height/2))
    screen.blit(gameOver, (width/2, height/2 - 100))
    pygame.display.update()
  else:
    if level.reset == True:
        level = Level(level_map, screen)
        level.reset = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    screen.blit(bg, bg.get_rect())
    level.run()
    
    pygame.display.update()
    clock.tick(60)
#---

while True:
    #for boss in level.bosses:
        #pygame.draw.rect(screen, color, boss.collideRect, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    screen.blit(bg, bg.get_rect())
    level.run()
    
    pygame.display.update()
    clock.tick(60)