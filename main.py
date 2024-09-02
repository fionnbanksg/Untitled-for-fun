import pygame
import sys
from game_manager import GameManager

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Infinite Terrain with Camera and Player")

    game_manager = GameManager(width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_manager.player_jump()

        # Simulate player movement to the right with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            game_manager.move_player(5)
        if keys[pygame.K_LEFT]:
            game_manager.move_player(-5)

        # Update game components
        game_manager.update_game_components(screen)

        # Update display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
