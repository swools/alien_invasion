import pygame

class Link:
    """A class for Zelda's Link"""

    def __init__(self, blue_sky):

        self.screen = blue_sky.screen
        self.screen_rect = blue_sky.screen.get_rect()

        self.image = pygame.image.load('images/link.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)