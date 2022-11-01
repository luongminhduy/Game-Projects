from cmath import cos
from email.mime import image
from tkinter import CENTER
import config
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.sprite = pygame.image.load('./assets/Enemy/porkim.png')
        self.image = self.sprite.subsurface(56, 146, 112, 80)
        self.rect = self.image.get_rect(bottomleft =(pos[0],pos[1]+40))
        self.flipImage = pygame.transform.flip(self.image, True, False)
        self.status = 'idle'
        self.frame = 0
        self.countFrame = 0
        self.animations = {'idle': [], 'run':[], 'attack':[]}
        self.flipAnimations = {'idle': []}
        self.import_enemy_assets()
        self.direction = pygame.Vector2((0,0))
        self.right_moving = False

    def import_enemy_assets(self):
        for i in range(0, 5):
            img = pygame.transform.scale(self.sprite.subsurface(56 + 0, 146 + i * 224, 112, 80),(64,50))
            self.animations['idle'].append(img)
            self.flipAnimations['idle'].append(pygame.transform.flip(img, True, False))
    
    def animate(self):
        if self.countFrame % 10 == 0:
            self.frame = (self.frame + 1) % 5
            if (self.right_moving):
                self.image = self.flipAnimations['idle'][self.frame]
            else:
                self.image = self.animations['idle'][self.frame]
            
    def die(self):
        self.kill()

    def run(self):
        if (self.countFrame % 300 < 150):
            self.rect.x -= 1
            self.right_moving = False
        else: 
            self.rect.x += 1
            self.right_moving = True
        
        
    def update(self, x_shift):
        self.rect.x += x_shift
        self.countFrame = self.countFrame + 1
        self.run()
        self.animate()
        

    

