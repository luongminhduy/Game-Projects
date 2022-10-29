import string
import pygame

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, pos, size, type:string) -> None:
        super().__init__()
        
        if type == "Dirt":
            self.image = pygame.transform.scale(pygame.image.load("./assets/Tiles/Dirt.png"),(size,size))
        else: 
            self.image = pygame.transform.scale(pygame.image.load("./assets/Tiles/GrassJoinHillLeft2.png"),(size,size))
            
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, x_shift):
        self.rect.x += x_shift # type: ignore