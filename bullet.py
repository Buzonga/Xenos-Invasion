import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, xi_game):
        super().__init__()

        self.screen = xi_game.screen
        self.settings = xi_game.settings
        self.colour = self.settings.bullet_colour

        self.rect = pg.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = xi_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):

        pg.draw.rect(self.screen, self.colour, self.rect)