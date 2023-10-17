class Settings():
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize game settings. """
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 100, 100
        self.bullets_allowed = 3