import pytest
from glider.models import Glider

def test_glider_cell_coordinates():
    pattern = [
        [1, 0],
        [1, 1]
    ]
    g = Glider(id="g1", pattern=pattern, x=2, y=3)

    expected_cells = {(2,3), (2,4), (3,4)}
    actual_cells = set(g.get_cells())

    assert actual_cells == expected_cells

def test_glider_movement():
    pattern = [
        [1]
    ]
    g = Glider(id="g2", pattern=pattern, x=0, y=0, dx=1, dy=2)
    g.move()
    assert g.x == 1
    assert g.y == 2