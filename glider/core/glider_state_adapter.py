# glider/core/glider_state_adapter.py

class GliderStateAdapter:
    """
    Translates between GliderEngine internal grid and the JSON format
    expected by the frontend ( { 'gliders': [ { 'cells': [[x,y], …] } ] } ).
    """

    def __init__(self, engine):
        self.engine = engine

    # export - json to front end
    def to_json_payload(self):
        """Return a dict ready for jsonify()"""
        cells = [
            [x, y]
            for y, row in enumerate(self.engine.grid)
            for x, cell in enumerate(row)
            if cell
        ]
        return {"status": "ok", "gliders": [{"cells": cells}]}


class GliderStateAdapter3D:
    """
    Translates between BlobEngine internal grid and the JSON format
    expected by the frontend ( { 'blobs': [ { 'cubes': [[z,y,x], …] } ] } ).
    """
    def __init__(self, engine):
        self.engine = engine

    def to_json_payload(self, radius=2):
        """
        Return a serializable dict containing dense 3D matrix from get_render_slice().
        """
        matrix = self.engine.get_render_slice(radius=radius)
        return {
            "center": self.engine.center,
            "generation": self.engine.generation,
            "matrix": matrix
        }