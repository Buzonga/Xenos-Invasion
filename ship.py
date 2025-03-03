import pygame as pg

class Ship():

    def __init__(self, xi_game):
        
        self.screen = xi_game.screen
        self.settings = xi_game.settings
        self.screen_rect = xi_game.screen.get_rect()

        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.screen_rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):

        self.screen.blit(self.image, self.rect)