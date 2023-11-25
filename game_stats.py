class GameStats():
    """Tracks statistics for the game."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True

        # Start game in an inactive state.
        self.game_active = False

        # High score that should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0