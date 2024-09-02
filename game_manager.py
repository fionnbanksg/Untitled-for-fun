import terrain
import pygame
from camera import Camera
from player import Player

# Colors
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

class GameManager:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.camera = Camera(width, height)
        self.player = Player(x=100, y=100)
        self.terrain_segments = []
        self.last_segment_end = 0
        self.supersample_factor = 2  # Factor to increase resolution by
        self.high_res_surface = pygame.Surface(
            (self.screen_width * self.supersample_factor, self.screen_height * self.supersample_factor)
        )
        print("GameManager initialized.")

    def generate_and_store_terrain(self):
        if self.last_segment_end - self.player.x < self.screen_width:
            new_segment = terrain.generate_terrain_segment(self.last_segment_end, terrain.segment_width)
            self.terrain_segments.append(new_segment)
            self.last_segment_end += terrain.segment_width

    def prune_terrain(self):
        visible_start_x = self.camera.camera_x - terrain.segment_width
        self.terrain_segments = [
            segment for segment in self.terrain_segments 
            if segment[-1][0] >= visible_start_x
        ]

    def update_game_components(self, screen):
        self.camera.update(self.player.x)
        self.generate_and_store_terrain()
        self.prune_terrain()

        # Fill the high-resolution surface
        self.high_res_surface.fill(BLACK)

        # Scale the coordinates for the high-res surface
        visible_terrain = [
            [(x * self.supersample_factor, y * self.supersample_factor) for x, y in segment]
            for segment in self.camera.apply_to_terrain(self.terrain_segments)
        ]

        # Draw on the high-resolution surface
        for segment in visible_terrain:
            pygame.draw.aalines(self.high_res_surface, GREEN, False, segment)

        # Draw the player
        self.player.update(self.terrain_segments)
        self.player.draw(self.high_res_surface, self.camera)

        # Scale down the high-res surface to fit the screen
        scaled_surface = pygame.transform.smoothscale(
            self.high_res_surface, (self.screen_width, self.screen_height)
        )

        # Blit the scaled surface onto the screen
        screen.blit(scaled_surface, (0, 0))

    def move_player(self, dx):
        self.player.move(dx)

    def player_jump(self):
        self.player.jump()
