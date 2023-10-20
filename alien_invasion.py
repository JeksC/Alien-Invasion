
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialise pygame, settings  and screen object
    pygame.init()
    ai_settings = Settings()   #Loads settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings,screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make a group to store aliens in.
    aliens = Group()

    # Make a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # Redraw the screen during each pass through the loop.
        gf.update_bullets(aliens, bullets)  
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
