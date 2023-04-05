import random
import sys
import pygame, time
from pygame.locals import *

from settings import Settings
from test_rect import TestRect
from spritesheet import SpriteSheet
from debug import debug
from player import Player
from gun import Gun
from slime import Slime
from explosion_slime import SlimeExplosion
from bullet import Bullet
from cursor import Cursor

class td_Shooter():
    """Overall Class to manage game assets and behaviour"""
    
    def __init__(self):
        pygame.init()
        # Load settings
        self.settings = Settings()

        # Set time
        self.clock = pygame.time.Clock()
        self.previous_time = time.time()

        # Display a screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("td_Shooter")
        self.screen_rect = self.screen.get_rect()

        # Set background
        self.bg_colour = self.settings.bg_colour
        self.bg_image = self.settings.bg_image

        # Spawn chance
        self.spawn_chance = self.settings.slime_spawn_chance

        # Initialise assets
        self.cursor = Cursor(self)
        self.player = Player(self)
        self.gun = Gun(self)
        self.slimes = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

    def run_game(self):
        """The main game loop"""
        while True:
            self.clock.tick(60)
            self.check_events()
            self.cursor.update_cursor()
            self.player.update()
            self.gun.update()
            self.slimes.update()
            self.update_bullets()
            self.explosions.update()
            self.spawn_slime()
            self.update_screen()

    def update_screen(self):
        """Update images on screen and flip to new screen"""
        self.screen.blit(self.bg_image, (0, 0))
        self.cursor.blit_cursor()
        self.player.blitme()
        self.gun.blitme()
        for slime in self.slimes:
            slime.blitme()
        for bullet in self.bullets:
            bullet.blitme()
        for explosion in self.explosions:
            explosion.blitme()

        pygame.display.flip()

    def check_events(self):
        """Respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousedown_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_mouseup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key down presses"""
        # Movement
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_w:
            self.player.moving_up = True
        elif event.key == pygame.K_s:
            self.player.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # Movement
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_w:
            self.player.moving_up = False
        elif event.key == pygame.K_s:
            self.player.moving_down = False

    def _check_mousedown_events(self, event):
        """Respond to mouse down presses"""
        # Shooting
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._fire_bullet()

    def _check_mouseup_events(self, event):
        """Respond to mouse up presses"""
        # Shooting
        # if event.type == pygame.MOUSEBUTTONUP:

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Updates position of bullets"""
        self.bullets.update()
        # Get rid of disappeared ones
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
            if bullet.rect.right < 0:
                self.bullets.remove(bullet)
            if bullet.rect.top > self.screen_rect.bottom:
                self.bullets.remove(bullet)
        self._bullet_slime_collisions()

    def spawn_slime(self):
        """Spawns a slime in a random position"""
        # Get a random x, y position
        self.x = random.randint(10, self.settings.screen_width - 10)
        self.y = random.randint(10, self.settings.screen_height - 10)
        # Roll the spawn chance dice
        self.chance = random.randint(1, self.spawn_chance)
        # If it hits, make a new slime
        if self.chance == 1:
            self.new_slime = Slime(self, self.x, self.y)
            # If there's not too many slimes:
            if len(self.slimes) < self.settings.slime_limit:
                # If the x&y doesn't overlap an existing slime
                if not pygame.sprite.spritecollide(self.new_slime, self.slimes, False):
                    self.slimes.add(self.new_slime)

    def player_collisions(self):
        """Manage player collisions with enemies"""

    def _bullet_slime_collisions(self):
        """Manage bullet and slime collisions"""
        collisions = pygame.sprite.groupcollide(self.slimes, self.bullets, False, True)
        if collisions:
            for hit_slime in collisions.keys():
                hit_slime.health -= self.settings.bullet_damage
                if hit_slime.health <= 0:
                    new_explosion = SlimeExplosion(self, hit_slime.rect)
                    self.explosions.add(new_explosion)


if __name__ == "__main__":
    game = td_Shooter()
    game.run_game()