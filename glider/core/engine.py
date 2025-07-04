# glider/core/engine.py

class GliderEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def step(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                alive = self.grid[y][x]
                neighbors = self._count_neighbors(x, y)

                if alive:
                    if neighbors in (2, 3):
                        new_grid[y][x] = 1
                else:
                    if neighbors == 3:
                        new_grid[y][x] = 1

        self.grid = new_grid

    def _count_neighbors(self, x, y):
        total = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    total += self.grid[ny][nx]
        return total

    def load_pattern(self, pattern, offset_x=0, offset_y=0):
        for dy, row in enumerate(pattern):
            for dx, cell in enumerate(row):
                if 0 <= offset_y + dy < self.height and 0 <= offset_x + dx < self.width:
                    self.grid[offset_y + dy][offset_x + dx] = cell

