import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, xi_game):
        super().__init__()
        self.screen = xi_game.screen
        self.settings = xi_game.settings

        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x