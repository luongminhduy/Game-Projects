import pygame
class Hammer:
    def __init__(self, sprite, range, audio) -> None:
        self.sprite = sprite
        self.range = range
        self.attack = False
        self.rotation = 0
        self.audio = audio
        self.size = (100, 100)
        

    def display(self, screen: pygame.Surface) -> None:
        (x, y) = pygame.mouse.get_pos()
        screen.blit(pygame.transform.scale(self.sprite, self.size), (x - 50, y - 50))

    def hit(self, x, y):
        self.attack = True
        self.rotation = 90
        pygame.mixer.Sound.play(self.audio)
        return (x + 90, y + 90, self.range)

    def unHit(self):
        self.attack = False
        self.rotation = -90

    def changeAnimation(self):
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)

