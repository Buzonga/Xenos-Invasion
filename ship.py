import pygame as pg

class Ship():

    def __init__(self, xi_game):
        
        self.screen = xi_game.screen
        self.screen_rect = xi_game.screen.get_rect()

        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)