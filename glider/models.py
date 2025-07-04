# glider/models.py

class Glider:
    def __init__(self, id, pattern, x, y, dx=1, dy=0):
        self.id = id
        self.pattern = pattern  # 2D list of 0/1
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def get_cells(self):
        return [
            (self.x + dx, self.y + dy)
            for dy, row in enumerate(self.pattern)
            for dx, cell in enumerate(row) if cell
        ]