import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.image.load('./assets/Enemy/fire.png')
        self.rect = self.image.get_rect(topleft =pos)

    def fly(self):
        self.rect.x -= 3
        