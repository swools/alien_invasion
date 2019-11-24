import sys
import pygame

from game_character import Link

class BlueSky:

    def __init__(self):

        pygame.init()
        
        self.screen = pygame.display.set_mode((800, 1200))
        self.link = Link(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

            self.screen.fill((10, 230, 230))
            self.link.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
