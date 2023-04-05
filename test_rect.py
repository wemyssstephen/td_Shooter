import pygame
import time

class TestRect():
    """A test rectangle used to learn deltatime"""
    
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.previous_time = game.previous_time
    
        # Create rect, store position, set direction
        self.test_rect = pygame.Rect(0,310,100,100)
        self.pos = pygame.math.Vector2(self.test_rect.topleft)
        self.direction = 1

    def update(self):
        """Movement for the test rectangle"""
        # Getting the delta time. Previous time initialised in td_Shooter init outside game loop.
        self.dt = time.time() - self.previous_time
        self.previous_time = time.time()
        # test_rect movement using delta time
        self.pos.x += self.direction * self.settings.test_speed * self.dt
        # Update position using x
        self.test_rect.x = round(self.pos.x)

    def _draw_test_rect(self):
        """Draw the test rectangle"""
        pygame.draw.rect(self.screen, 'red', self.test_rect)