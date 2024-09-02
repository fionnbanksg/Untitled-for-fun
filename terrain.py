import noise

# Parameters for Perlin noise
scale = 1000
octaves = 4
persistence = 0.5
lacunarity = 2.0
y_offset = 300
segment_width = 100

def generate_terrain_segment(start_x, segment_width):
    terrain = []
    for x in range(start_x, start_x + segment_width):
        y = noise.pnoise1(x / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
        y = int((y + 0.5) * 100) + y_offset
        terrain.append((x, y))
    return terrain
