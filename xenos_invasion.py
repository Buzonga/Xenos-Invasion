import sys
import pygame as pg

class XenosInvasion:

    def __init__(self):
        pg.init()

        self.screen - pg.display.set_mode((1200, 800))
        pg.display.set_caption("Xenos Invasion")

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            pg.display.flip()

if __name__ == '__main__':
    xi = XenosInvasion()
    xi.run_game