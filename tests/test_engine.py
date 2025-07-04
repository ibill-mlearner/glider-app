import pytest
from glider.core.engine import GliderEngine

@pytest.fixture
def engine():
    return GliderEngine(5, 5)

def test_initial_grid_is_empty(engine):
    for row in engine.grid:
        assert row == [0, 0, 0, 0, 0]

def test_step_still_life_block():
    block = [
        [1, 1],
        [1, 1]
    ]
    engine = GliderEngine(4, 4)
    engine.load_pattern(block, 1, 1)
    prev = [row[:] for row in engine.grid]
    engine.step()
    assert engine.grid == prev

def test_step_blinker_oscillator():
    blinker1 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    blinker2 = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    engine = GliderEngine(5, 5)
    engine.load_pattern(blinker1, 1, 1)
    engine.step()
    for y in range(3):
        for x in range(3):
            assert engine.grid[y+1][x+1] == blinker2[y][x]