# glider/core/engine.py

class GliderEngine:
    """
    Game of Life Rules Summary:
    Counting method: _count_neighbors(self, x, y)
    Each cell has 8 neighbors (adjacent horizontally, vertically, and diagonally).
    A live cell survives if it has 2 or 3 live neighbors; otherwise it dies.
    A dead cell becomes alive only if it has exactly 3 live neighbors.
    This function counts the number of live neighbors around a given cell (x, y).
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]


    def tick(self):
        self.step()

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

    """Pattern expects a 2D array as binary to draw onto the grid."""
    def load_pattern(self, pattern, offset_x=0, offset_y=0):
        for dy, row in enumerate(pattern):
            for dx, cell in enumerate(row):
                if 0 <= offset_y + dy < self.height and 0 <= offset_x + dx < self.width:
                    self.grid[offset_y + dy][offset_x + dx] = cell

    def reset(self, pattern):
        """Reset the entire grid to all empty zeros. Redo-constructor* """
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.load_default_pattern(pattern)

    def load_default_pattern(self, pattern):
        offset_x = 2
        offset_y = (self.height // 2) - 1
        self.load_pattern(pattern,offset_x,offset_y)