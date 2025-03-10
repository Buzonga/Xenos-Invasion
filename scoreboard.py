import pygame as pg
import pygame.font

class Scoreboard:

    def __init__(self, xi_game):
        self.screen = xi_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = xi_game.settings
        self.stats = xi_game.stats

        self.text_colour = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_colour, self.settings.bg_colour)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_colour, self.settings.bg_colour)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.score.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()