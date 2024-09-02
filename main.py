import pygame
import sys
from game_manager import GameManager

def main():
    pygame.init()
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Infinite Terrain with Camera")

    game_manager = GameManager(width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game_manager.move_player(0.2)

        game_manager.update_game_components(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
