# glider/core/glider_state_adapter.py

class GliderStateAdapter:
    """
    Translates between GliderEngine internal grid and the JSON format
    expected by the frontend ( { 'gliders': [ { 'cells': [[x,y], …] } ] } ).
    """

    def __init__(self, engine):
        self.engine = engine

    # ─────────────────────────────────── export ──
    def to_json_payload(self):
        """Return a dict ready for jsonify()"""
        cells = [
            [x, y]
            for y, row in enumerate(self.engine.grid)
            for x, cell in enumerate(row)
            if cell
        ]
        return {"status": "ok", "gliders": [{"cells": cells}]}

    # ─────────────────────────────────── import ──
    def load_cells(self, cells):
        """
        Given a list of [x, y] pairs, reset grid and activate those cells.
        Useful for syncing external edits back into the engine.
        """
        height = len(self.engine.grid)
        width = len(self.engine.grid[0]) if height else 0

        # Clear grid
        for y in range(height):
            for x in range(width):
                self.engine.grid[y][x] = 0

        # Activate cells
        for x, y in cells:
            if 0 <= y < height and 0 <= x < width:
                self.engine.grid[y][x] = 1
