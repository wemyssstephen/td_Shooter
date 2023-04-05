import time
import pygame.math


class Settings:
    """A class to store all the settings for td_Shooter."""

    def __init__(self):
        """Initialise the static game settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_colour = (100, 100, 100)
        self.bg_image = pygame.image.load("assets/second_attempt.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
        
        # Sprite size
        self.player_width = 55
        self.player_height = 75
        self.slime_width = 55
        self.slime_height = 65
        self.explosion_width = 64
        self.explosion_height = 64
        
        # Speed settings
        self.test_speed = 500
        self.player_speed = 300
        self.bullet_speed = 20
        
        # Bullet settings
        self.bullets_allowed = 25
        self.bullet_offset_x = 50
        self.bullet_offset_y = 5
        self.bullet_damage = 25

        # Gun settings
        self.gun_offset_x = 30
        self.gun_offset_y = 10
        self.flipped_offset_x = 30
        self.flipped_offset_y = -5

        # Slime settings
        self.slime_limit = 5
        self.slime_speed = 2.5
        self.slime_spawn_chance = 30 # higher makes it less likely
        self.slime_health = 75