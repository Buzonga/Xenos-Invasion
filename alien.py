import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, xi_game):
        super().__init__()
        self.screen = xi_game.screen

        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
