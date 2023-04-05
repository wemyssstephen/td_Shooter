import math
import pygame

class Gun:
    """A class to handle gun movement"""
    def __init__(self, game):
        """Initalise all the assets"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.cursor = game.cursor
        self.player = game.player

        # Get image asset. Make a copy in base image and get its rect (centered on the player).
        self.image = pygame.image.load("assets/mg_side.png").convert()
        self.image = pygame.transform.scale(self.image, (45,18))
        self.base_image = self.image
        self.flipped_image = pygame.transform.flip(self.base_image, False, True)
        self.base_image_rect = self.base_image.get_rect(center = self.player.player_rect.center)

        # Set gun position
        self._set_gun_position()

    def update(self):
        """Rotate the gun towards the mouse"""
        # Make the gun follow the player
        self._get_rotation_angle()
        # Make the gun follow the mouse
        self._flip_gun_image()

    def _set_gun_position(self):
        """Sets the initial gun position"""
        # Get angles and offset vectors
        self._get_rotation_angle()
        self.offset = pygame.math.Vector2(self.settings.gun_offset_x, self.settings.gun_offset_y)
        self.flipped_offset = pygame.math.Vector2(self.settings.flipped_offset_x, self.settings.flipped_offset_y)

        # Set position on player + offset angle
        self.pos = pygame.math.Vector2(self.base_image_rect.center)
        self.pos = self.pos + self.offset.rotate(self.angle)
        self.base_image_rect.center = round(self.pos)
        self.image_rect = self.base_image_rect.copy()

    def _get_rotation_angle(self):
        """Get the angle for rotating the gun towards the mouse"""
        self.mouse_pos = self.cursor.mouse_pos
        self.radians = math.atan2(self.mouse_pos[1] - self.base_image_rect.y, self.mouse_pos[0] - self.base_image_rect.x)
        self.angle = math.degrees(self.radians)

    def _flip_gun_image(self):
        """Flip the gun image to face the right way when looking left"""
        if self.angle > 90 or self.angle < -90:
            self.base_image_rect = self.base_image.get_rect(center=self.player.player_rect.center)
            self.pos = pygame.math.Vector2(self.base_image_rect.center)
            self.pos = self.pos + self.flipped_offset.rotate(self.angle)
            self.base_image_rect.center = round(self.pos)

            self.image = pygame.transform.rotate(self.flipped_image, -self.angle)
            self.image_rect = self.image.get_rect(center=self.base_image_rect.center)
        else:
            self.base_image_rect = self.base_image.get_rect(center=self.player.player_rect.center)
            self.pos = pygame.math.Vector2(self.base_image_rect.center)
            self.pos = self.pos + self.offset.rotate(self.angle)
            self.base_image_rect.center = round(self.pos)

            self.image = pygame.transform.rotate(self.base_image, -self.angle)
            self.image_rect = self.image.get_rect(center=self.base_image_rect.center)

    def blitme(self):
        """Draw the gun at its current location"""
        self.screen.blit(self.image, self.image_rect)
        # Too see how the gun rectangles work:
        # pygame.draw.rect(self.screen, "yellow", self.image_rect, width=2)
        # pygame.draw.rect(self.screen, "red", self.base_image_rect, width=2)