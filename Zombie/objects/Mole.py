import pygame
from enum import Enum

class Constant:
    SPEED_DIE = 3
    SPEED_STAND = 100

class MoleAnimation(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    DIE = 3
    STAND = 4

class Mole:   
 
    def __init__(self, pos_x, pos_y, animation = MoleAnimation.NONE) -> None:
        super(Mole, self).__init__()
        self.animation = animation
        self.X = pos_x
        self.Y = pos_y
        self.up_frames = []
        self.up_idx = 0
        for i in range(1,11):
            self.up_frames.append(pygame.transform.scale(pygame.image.load('assets/up_' + str(i) + '.png'), (90,120)))
        
        self.down_frames = self.up_frames[::-1]
        self.down_idx = 0
        
        self.die_frames = []
        self.die_idx = 0
        for i in range(1,5):
            self.up_frames.append(pygame.transform.scale(pygame.image.load('assets/die_' + str(i) + '.png'), (90,120)))
            
        self.stand_frame = pygame.transform.scale(pygame.image.load('assets/up_10.png'), (90,120)) 
        self.stand_idx = 0
        
    def display(self, screen: pygame.Surface):
        match(self.animation):
            case MoleAnimation.NONE: 
                self.up_idx = self.down_idx = self.die_idx = self.stand_idx = 0
            
            case MoleAnimation.UP:
                if self.up_idx >= len(self.up_frames):
                    self.up_idx = 0
                    self.animation = MoleAnimation.STAND
                    screen.blit(self.stand_frame, (self.X, self.Y))
                else:
                    screen.blit(self.up_frames[self.up_idx], ((self.X, self.Y)))
                    self.up_idx += 1
                
            case MoleAnimation.DOWN:
                if self.down_idx >= len(self.down_frames):
                    self.down_idx = 0
                    self.animation = MoleAnimation.NONE
                else:
                    screen.blit(self.down_frames[self.down_idx], ((self.X, self.Y)))
                    self.down_idx += 1
            
            case MoleAnimation.DIE:
                if self.die_idx >= len(self.die_frames) * Constant.SPEED_DIE:
                    self.die_idx = 0
                    self.animation = MoleAnimation.NONE
                else:
                    screen.blit(self.die_frames[self.die_idx % Constant.SPEED_DIE], ((self.X, self.Y)))
                    self.die_idx += 1
                
            case MoleAnimation.STAND:
                if self.stand_idx >= Constant.SPEED_STAND:
                    self.stand_idx = 0
                    self.animation = MoleAnimation.DOWN
                else:
                    screen.blit(self.stand_frame, ((self.X, self.Y)))
                    self.stand_idx += 1       