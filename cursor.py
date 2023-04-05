import pygame

class Cursor:
    """A class to manage the cursor"""

    def __init__(self, game):
        """Initialise ----"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.previous_time = game.previous_time
        
        # Set the image
        self.image = pygame.image.load("assets/4crosshair.png")
        self.cursor_rect = self.image.get_rect()
        
        # Mouse pos
        self.mouse_pos = pygame.mouse.get_pos()
        
    def update_cursor(self):
        """Set cursor to crosshair"""
        pygame.mouse.set_visible(False)
        self.mouse_pos = pygame.mouse.get_pos()
        self.cursor_rect.x = self.mouse_pos[0] - self.cursor_rect.width / 2
        self.cursor_rect.y = self.mouse_pos[1] - self.cursor_rect.height / 2

    def blit_cursor(self):
        """Draw the cursor at position"""
        self.screen.blit(self.image, self.cursor_rect)
        
    