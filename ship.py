import pygame

class Ship():
    """Class that manages the behaviour of player's ship"""

    def __init__(self,screen):
        """Initialize the ship and its starting position."""
        self.screen = screen

        #Load the ship and get its rect (rectangle).
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

