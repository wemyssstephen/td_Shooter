import math
import pygame
import time
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet objects"""

    def __init__(self, game):
        """Initialise ----"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.cursor = game.cursor
        self.screen_rect = game.screen.get_rect()
        self.player_center = game.player.player_rect.center

        # Load an image and rectangle
        self.image = pygame.image.load("assets/bulletc.png")
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        
        # Set position on player
        self.rect.center = self.player_center
        self.pos = pygame.math.Vector2(self.rect.center)

        # Get the bullets angle to mouse position
        self._get_bullet_vector()

        # Offset bullet to gun
        self.offset = pygame.math.Vector2(self.settings.bullet_offset_x, self.settings.bullet_offset_y)
        self.pos = self.pos + self.offset.rotate(self.angle)

    def update(self):
        """Set the path of the bullet"""
        self.pos.x += self.dx
        self.pos.y += self.dy
        self.rect.center = round(self.pos)

    def _get_bullet_vector(self):
        """Get the bullet vector between player and cursor"""
        self.mouse_pos = self.cursor.mouse_pos
        self.radians = math.atan2(self.mouse_pos[1] - self.pos.y, self.mouse_pos[0] - self.pos.x)
        self.angle = math.degrees(self.radians)
        self.dx = math.cos(self.radians) * self.settings.bullet_speed
        self.dy = math.sin(self.radians) * self.settings.bullet_speed
        # Rotate image to the correct angle
        self.image = pygame.transform.rotate(self.image, -self.angle)
         
    def blitme(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)


            




        
        