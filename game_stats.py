class GameStats:
    def __init__(self, xi_game):
        self.settings = xi_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit