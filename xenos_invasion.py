import sys
import pygame as pg

from settings import Settings
from ship import Ship

class XenosInvasion:

    def __init__(self):

        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Xenos Invasion")

        self.ship = Ship(self)

        self.bg_colour = (230, 230, 230)

        # Hydra Dominatus!

    def run_game(self):

        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()

            self.clock.tick(60)

        # Hydra Dominatus!

    def _check_events(self):

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                # Movement events
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pg.K_LEFT:
                        self.ship.moving_left = True

                elif event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pg.K_LEFT:
                        self.ship.moving_left = False

        # Hydra Dominatus!

    def _update_screen(self):
         
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()

        pg.display.flip()

        # Hydra Dominatus!
         

if __name__ == '__main__':

    xi = XenosInvasion()
    xi.run_game()

    # Hydra Dominatus!