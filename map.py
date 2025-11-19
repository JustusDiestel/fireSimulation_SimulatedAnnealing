import random

class Map():

    def __init__(self,height: int, width: int):
        self.width = width
        self.height = height
        self.my_map = [[0 for i in range(width)] for i in range(height)]

    def create_heat_map(self):
        self.my_map = [[self.random_rot() for i in range(self.width)] for i in range(self.height)]

    def random_rot(self) -> int:
        return random.randint(0, 255)

    def print_map(self):
        for row in self.my_map:
            print(row)

    def current_state(self):
        return [row[:] for row in self.my_map]

import random

def choose_random_px(heatmap: list[list[int]], height: int, width: int) -> tuple[int, int]:
    y = random.randrange(height)
    x = random.randrange(width)
    return (y, x)

def mutate_random_px(heatmap: list[list[int]], height: int, width: int) -> list[list[int]]:
    y, x = choose_random_px(heatmap, height, width)
    px = heatmap[y][x]
    mutation = random.randint(-20, 20)
    px += mutation

    if px > 255:
        px = 255
    elif px < 0:
        px = 0

    heatmap[y][x] = px

    return heatmap






