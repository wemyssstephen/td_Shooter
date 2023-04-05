import pygame
import math
import time
from spritesheet import SpriteSheet
from pygame.sprite import Sprite

class Player(Sprite):
    """A class to manage the player"""

    def __init__(self, game):
        """Initialise the player and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.bg_colour = game.bg_colour
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.previous_time = game.previous_time

        # Get mouse position
        self.cursor = game.cursor

        # Get player image & animations
        self.current_image = 0
        self._get_anims()
        self.player = self.anim_s[int(self.current_image)]

        # Get player rectangle
        self.player_rect = self.player.get_rect()

        # Set position to centre
        self.player_rect.center = self.screen_rect.center
        self.pos = pygame.math.Vector2(self.player_rect.center)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update player movement and image"""
        # Getting the delta time. previous_time initialised in td_Shooter outside game loop.
        self.dt = time.time() - self.previous_time
        self.previous_time = time.time()
        # Player movement and set p[layer image on mouse position
        self._get_rotation_angle()
        self.player_movement(self.dt)
        self.player_image()

    def get_center(self):
        return self.player_rect.x + self.settings.player_width / 2, \
            self.player_rect.y + self.settings.player_height / 2

    def player_movement(self, dt):
        """Defines player movement"""
        # Player movement instructions
        if self.moving_right and self.player_rect.right < self.screen_rect.right:
            self.pos.x += self.settings.player_speed * self.dt
            self.player_rect.x = round(self.pos.x)
            self.current_image += 0.2

        if self.moving_left and self.player_rect.left > 0:
            self.pos.x -= self.settings.player_speed * self.dt
            self.player_rect.x = round(self.pos.x)
            self.current_image += 0.2

        if self.moving_up and self.player_rect.top > 0:
            self.pos.y -= self.settings.player_speed * self.dt
            self.player_rect.y = round(self.pos.y)
            self.current_image += 0.2

        if self.moving_down and self.player_rect.bottom < self.screen_rect.bottom:
            self.pos.y += self.settings.player_speed * self.dt
            self.player_rect.y = round(self.pos.y)
            self.current_image += 0.2

    def player_image(self):
        """Define the shown player image depending on where the mouse is facing"""

        if self.angle < 45 and self.angle > -45:
            if self.current_image >= len(self.anim_r):
                self.current_image = 0
            self.player = self.anim_r[int(self.current_image)]

        if self.angle < -45 and self.angle > -135:
            if self.current_image >= len(self.anim_n):
                self.current_image = 0
            self.player = self.anim_n[int(self.current_image)]

        if self.angle < -135 or self.angle > 135:
            if self.current_image >= len(self.anim_l):
                self.current_image = 0
            self.player = self.anim_l[int(self.current_image)]

        if self.angle < 135 and self.angle > 45:
            if self.current_image >= len(self.anim_s):
                self.current_image = 0
            self.player = self.anim_s[int(self.current_image)]

    def _get_anims(self):
        """Get animations for player character"""
        # Moving down
        self.sprite_sheet_south = SpriteSheet(self, "assets/2_south.png")
        self.anim_s = []
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(0, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(1, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(2, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(3, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))

        # Moving up
        self.sprite_sheet_north = SpriteSheet(self, "assets/2_north.png")
        self.anim_n = []
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(0, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(1, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(2, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(3, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))

        # Moving right
        self.sprite_sheet_right = SpriteSheet(self, "assets/2_side.png")
        self.anim_r = []
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(0, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(1, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(2, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(3, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))

        # Moving left
        self.sprite_sheet_left = SpriteSheet(self, "assets/2_side.png")
        self.sprite_sheet_left.sprite_sheet = pygame.transform.flip(self.sprite_sheet_left.sprite_sheet, True, False)
        self.anim_l = []
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(0, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(1, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(2, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(3, 19, 0, 19, 24, self.settings.player_width, self.settings.player_height))

    def _get_rotation_angle(self):
        """Get the angle for rotating the gun towards the mouse"""
        self.mouse_pos = self.cursor.mouse_pos
        self.radians = math.atan2(self.mouse_pos[1] - self.player_rect.y, self.mouse_pos[0] - self.player_rect.x)
        self.angle = math.degrees(self.radians)

    def blitme(self):
        """Draw the player at its current location"""
        self.screen.blit(self.player, self.player_rect)