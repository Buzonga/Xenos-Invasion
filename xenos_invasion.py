import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet

class XenosInvasion:

    def __init__(self):

        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Xenos Invasion")

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

        self.bg_colour = (230, 230, 230)

        # Hydra Dominatus!

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
            self.clock.tick(60)

        # Hydra Dominatus!

    def _check_events(self):

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pg.KEYUP:
                    self._check_keyup_events(event)

        # Hydra Dominatus!

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_UP:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pg.K_UP:
            self.ship.moving_up = False
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):

        self.bullets.update()

        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _update_screen(self):
         
        self.screen.fill(self.settings.bg_colour)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pg.display.flip()

        # Hydra Dominatus!
         

if __name__ == '__main__':

    xi = XenosInvasion()
    xi.run_game()

    # Hydra Dominatus!