import terrain
import pygame
from camera import Camera

# Colors
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

class GameManager:
    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.camera = Camera(width, height)
        self.player_x = 0
        self.terrain_segments = []
        self.last_segment_end = 0
        print("GameManager initialized.")

    def generate_and_store_terrain(self):
        if self.last_segment_end - self.player_x < self.screen_width:
            new_segment = terrain.generate_terrain_segment(self.last_segment_end, terrain.segment_width)
            self.terrain_segments.append(new_segment)
            self.last_segment_end += terrain.segment_width

    def prune_terrain(self):
        # Remove segments that are completely off the screen
        visible_start_x = self.camera.camera_x - terrain.segment_width
        self.terrain_segments = [
            segment for segment in self.terrain_segments 
            if segment[-1][0] >= visible_start_x
        ]

    def update_game_components(self, screen):
        self.camera.update(self.player_x)
        self.generate_and_store_terrain()
        self.prune_terrain()  # Remove old, off-screen segments
        screen.fill(BLACK)

        visible_terrain = self.camera.apply_to_terrain(self.terrain_segments)
        for segment in visible_terrain:
            pygame.draw.lines(screen, GREEN, False, segment, 2)

    def move_player(self, dx):
        self.player_x += dx
