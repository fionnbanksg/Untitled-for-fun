class Camera:
    def __init__(self, width, height):
        self.camera_x = 0 
        self.width = width
        self.height = height

    def update(self, player_x):
        self.camera_x = player_x - self.width // 2 

    def apply(self, position):
        x, y = position
        return x - self.camera_x, y

    def apply_to_terrain(self, terrain_segments):
        return [[self.apply(point) for point in segment] for segment in terrain_segments]
