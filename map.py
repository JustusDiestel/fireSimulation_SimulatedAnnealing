import random
import math

class HeatMap:
    def __init__(self, height: int, width: int):
        self.width = width
        self.height = height
        self.my_map = [[0 for _ in range(width)] for _ in range(height)]

    def fill_random(self):
        self.my_map = [
            [self.random_val() for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def random_val(self) -> int:
        return random.randint(0, 255)

    def copy(self):
        return [row[:] for row in self.my_map]

    def mutate_random_px(self):
        y = random.randrange(self.height)
        x = random.randrange(self.width)

        val = self.my_map[y][x]
        val += random.randint(-20, 20)
        val = max(0, min(255, val))
        self.my_map[y][x] = val

    def print(self):
        for row in self.my_map:
            print(row)

    def cost(self) -> float:
        c = 0.0

        for y in range(self.height - 1):
            for x in range(self.width - 1):
                diff1 = abs(self.my_map[y][x] - self.my_map[y][x + 1])
                diff2 = abs(self.my_map[y][x] - self.my_map[y + 1][x])
                c += diff1 + diff2

        for y in range(self.height):
            desired = int(255 * (y / self.height))
            for x in range(self.width):
                c += abs(self.my_map[y][x] - desired)

        return c

    @staticmethod
    def make_proposal(current: "HeatMap") -> "HeatMap":
        proposal = HeatMap(current.height, current.width)
        proposal.my_map = current.copy()
        proposal.mutate_random_px()
        return proposal

    @staticmethod
    def annealing_step(current: "HeatMap", T: float) -> tuple["HeatMap", float]:
        proposal = HeatMap.make_proposal(current)

        old_cost = current.cost()
        new_cost = proposal.cost()

        if new_cost < old_cost:
            return proposal, new_cost

        prob = math.exp(-(new_cost - old_cost) / T)
        if random.random() < prob:
            return proposal, new_cost

        return current, old_cost

    @staticmethod
    def cool(T: float, factor: float = 0.99) -> float:
        return T * factor

    def run_annealing(self, iterations: int = 10000):
        self.fill_random()

        h = self
        T = 1.0
        current_cost = h.cost()

        for i in range(iterations):
            h, current_cost = HeatMap.annealing_step(h, T)
            T = HeatMap.cool(T, 0.999)

            if i % 1000 == 0:
                print(f"iter {i}, cost = {current_cost:.2f}, T = {T:.4f}")

        return h