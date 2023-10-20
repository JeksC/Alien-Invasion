class GameStats():
    """Tracks statistics for the game."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit