import noise
import random
# Parameters for Perlin noise
scale = 1000
octaves = 2
persistence = 0.5
lacunarity = 2.0
y_offset = 300
amplitude = 250 
segment_width = 100

seed_value = 42  

def generate_terrain_segment(start_x, segment_width):
    terrain = []
    random.seed(seed_value)  # Seed the random generator
    for x in range(start_x, start_x + segment_width):
        y = noise.pnoise1(x / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeat=1024, base=seed_value)
        y = int((y * amplitude) + y_offset)
        terrain.append((x, y))
    return terrain