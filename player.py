import pygame

class Player:
    def __init__(self, x, y, width=50, height=30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # Red color for the player
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.on_ground = False

    def move(self, dx):
        self.x += dx

    def jump(self):
        if self.on_ground:
            self.velocity = self.jump_strength
            self.on_ground = False

    def apply_gravity(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def check_collision(self, terrain_segments):
        for segment in terrain_segments:
            for point in segment:
                if self.x <= point[0] <= self.x + self.width:
                    if self.y + self.height >= point[1]:
                        self.y = point[1] - self.height
                        self.velocity = 0
                        self.on_ground = True
                        return

        self.on_ground = False

    def update(self, terrain_segments):
        self.apply_gravity()
        self.check_collision(terrain_segments)

    def draw(self, screen, camera):
        camera_x, camera_y = camera.apply((self.x, self.y))
        pygame.draw.rect(screen, self.color, (camera_x, camera_y, self.width, self.height))
