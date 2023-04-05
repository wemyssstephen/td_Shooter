import pygame
import math
import time
from debug import debug
from spritesheet import SpriteSheet
from pygame.sprite import Sprite

class SlimeExplosion(Sprite):
    """A class to hold the explosion when a slime dies"""
    def __init__(self, game, slime_rect):
        super().__init__()
        self.screen = game.screen
        self.bg_colour = game.bg_colour
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.previous_time = game.previous_time
        self.slime_rect = slime_rect
        self.explosions = game.explosions

        self.current_image = 0
        self._get_anims()
        self.explosion_image = self.anim_d[int(self.current_image)]

        self.rect = self.explosion_image.get_rect()
        self.rect.center = self.slime_rect.center

    def update(self):
        """Update animation"""
        self.explosion_image = self.anim_d[int(self.current_image)]
        self.current_image += 0.1
        if self.current_image >= len(self.anim_d):
            self.current_image == 0
            self.explosions.remove(self)

    def _get_anims(self):
        """Get the death animation"""
        # Death
        self.sprite_sheet_death = SpriteSheet(self, "assets/death.png")
        self.anim_d = []
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(0, 32, 0, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(1, 32, 0, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(2, 32, 0, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(0, 32, 32, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(1, 32, 32, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(2, 32, 32, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(0, 32, 64, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))
        self.anim_d.append(self.sprite_sheet_death._get_sprite_image(1, 32, 64, 32, 32, self.settings.explosion_width,
                                                                     self.settings.explosion_height))

    def blitme(self):
        self.screen.blit(self.explosion_image, self.rect)