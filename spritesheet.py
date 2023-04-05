import pygame

class SpriteSheet():
    """A class to handle all spritesheets"""
    def __init__(self, game, sprite_sheet):
        self.screen = game.screen
        self.sprite_sheet = pygame.image.load(sprite_sheet).convert()
        self.settings = game.settings

    def _get_sprite_image(self, frame, x, y, width, height, image_width, image_height):
        """Split up the sprite sheet. x&y denote the place on the sprite sheet to start the cut.
            width&height tell it how much to cut."""
        # Create an empty surface. Make it transparent. Get its rect.
        self.sprite = pygame.Surface((width, height)).convert()
        self.sprite.set_colorkey((0,0,0))
        self.sprite_rect = self.sprite.get_rect()

        # Draw the correct sprite using 'frame * x' onto the empty surface.
        self.sprite.blit(self.sprite_sheet, self.sprite_rect, (frame*x, y, width, height))
        self.sprite = pygame.transform.scale(self.sprite, (image_width, image_height))

        # Return the drawn on surface.
        return self.sprite