import pygame
import sys

class Keys:
    """Game that will print the key type you press"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))

    def run_game(self):
        """Start the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            self.screen.fill((250,250,250))
            pygame.display.flip()

if __name__ == '__main__':
    kg = Keys()
    kg.run_game()