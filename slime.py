import pygame
import math
import time
from debug import debug
from spritesheet import SpriteSheet
from pygame.sprite import Sprite

class Slime(Sprite):
    def __init__(self, game, x, y):
        """Initialise a slime and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.bg_colour = game.bg_colour
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.previous_time = game.previous_time

        # Get player
        self.player = game.player
        self.slimes = game.slimes

        # Get slime image & animations
        self.current_image = 0
        self._get_anims()
        self.slime_image = self.anim_s[int(self.current_image)]

        # Get slime rectangle
        self.rect = self.slime_image.get_rect()

        # Set position to centre
        self.rect.center = (x, y)
        self.pos = pygame.math.Vector2(self.rect.center)
        
        # Set slime health
        self.health = self.settings.slime_health

    def update(self):
        """Update slime movements"""
        if self.health <= 0:
            self.slimes.remove(self)
        else:
            self._get_player_vector()
            self._slime_movement()
            self.current_image += 0.1
            self._slime_anim()

    def _get_player_vector(self):
        """Get the angle and movement vector between the slime and the player"""
        self.player_center = self.player.player_rect.center
        self.radians = math.atan2(self.player_center[1] - self.pos.y, self.player_center[0] - self.pos.x)
        self.angle = math.degrees(self.radians)
        self.dx = math.cos(self.radians) * self.settings.slime_speed
        self.dy = math.sin(self.radians) * self.settings.slime_speed

    def _slime_movement(self):
        """Manage all slime movement"""
        self.pos.x += self.dx
        self.pos.y += self.dy

        # Repel if collide with another slime
        collisions = pygame.sprite.spritecollideany(self, self.slimes)
        if collisions:
            self.repel = pygame.math.Vector2()
            self.max_repel_distance = math.sqrt((self.slime_image.get_width() ** 2) + (self.slime_image.get_height() ** 2)) // 2
            offset = collisions.pos - self.pos
            if offset.magnitude() <= self.max_repel_distance:
                self.repel += (offset * (self.max_repel_distance - offset.magnitude())) // 3
            self.pos += self.repel

        self.rect.center = round(self.pos)

    def _slime_anim(self):
        """Alive alime animations"""
        if self.current_image >= len(self.anim_s):
            self.current_image = 0
        self.slime_image = self.anim_s[int(self.current_image)]

    def _get_anims(self):
        """Get animations for slime character"""
        # Moving down
        self.sprite_sheet_south = SpriteSheet(self, "assets/slime1_front.png")
        self.anim_s = []
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(0, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(1, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(2, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_s.append(self.sprite_sheet_south._get_sprite_image(3, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))

        # Moving up
        self.sprite_sheet_north = SpriteSheet(self, "assets/slime1_back.png")
        self.anim_n = []
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(0, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(1, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(2, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_n.append(self.sprite_sheet_north._get_sprite_image(3, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))

        # Moving right
        self.sprite_sheet_right = SpriteSheet(self, "assets/slime1_side.png")
        self.sprite_sheet_right.sprite_sheet = pygame.transform.flip(self.sprite_sheet_right.sprite_sheet, True, False)
        self.anim_r = []
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(0, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(1, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(2, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_r.append(self.sprite_sheet_right._get_sprite_image(3, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))

        # Moving left
        self.sprite_sheet_left = SpriteSheet(self, "assets/slime1_side.png")
        self.anim_l = []
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(0, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(1, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(2, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))
        self.anim_l.append(self.sprite_sheet_left._get_sprite_image(3, 16, 0, 16, 16, self.settings.slime_width, self.settings.slime_height))

    def blitme(self):
        """Draw the player at its current location"""
        self.screen.blit(self.slime_image, self.rect)
        # pygame.draw.rect(self.screen, "yellow", self.rect, width=2)