from cmath import cos
from email.mime import image
from tkinter import CENTER
import config
import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.sprite = pygame.image.load('./assets/Enemy/tucano.png')
        self.image = self.sprite.subsurface(0, 0, 224 , 224)
        self.rect = self.image.get_rect(topleft = pos)
        x, y = pos
        self.collideRect = pygame.rect.Rect((x, y + 56), (112, 112))
        self.flipX = x + 50
        self.flipImage = pygame.transform.flip(self.image, True, False)
        self.status = 'idle'
        self.frame = 0
        self.countFrame = 0
        self.animations = {'idle': [], 'run':[], 'attack':[]}
        self.flipAnimations = {'idle': []}
        self.attack = False
        self.hp = 2
        self.import_enemy_assets()
        self.direction = pygame.Vector2((0,0))
        self.right_moving = False
        print('boss create')

    def import_enemy_assets(self):
        for i in range(0, 5):
            img = self.sprite.subsurface(0 + i * 224, 0 , 224, 224)
            self.animations['idle'].append(img)
            self.flipAnimations['idle'].append(pygame.transform.flip(img, True, False))
    
    def animate(self):
        if self.countFrame % 10 == 0:
            if (self.attack == False):
                self.frame = (self.frame + 1) % 4
            if (self.right_moving):
                self.image = self.flipAnimations['idle'][self.frame]
                self.collideRect.x = self.rect.x + 60 
            else:
                self.image = self.animations['idle'][self.frame]
            
    def die(self):
        self.kill()

    def run(self):
        if (self.countFrame % 400 < 200):
            self.rect.x -= 1
            self.collideRect.x -= 1
            self.right_moving = False
        else: 
            self.rect.x += 1
            self.collideRect.x += 1
            self.right_moving = True
        if (self.attack):
            self.rect.y += 2
            self.collideRect.y += 2
            self.frame = 4
        else:
            self.rect.y -= 2
            self.collideRect.y -= 2

    def attacking(self):
        if (self.countFrame % 100 == 0):
            self.attack = True
        if (self.countFrame % 100 == 50):
            self.attack = False

        
    def update(self, x_shift):
        self.rect.x += x_shift
        self.collideRect.x += x_shift
        self.countFrame = self.countFrame + 1
        self.animate()
        self.run()
        self.attacking()
        
