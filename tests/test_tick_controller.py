# tests/test_tick_controller.py

import pytest
from glider.core import tick_controller

def test_apply_tick_empty_grid():
    initial = []
    updated = tick_controller.apply_tick(initial)
    assert updated == []

def test_apply_tick_static_block():
    block = [(1, 1), (1, 2), (2, 1), (2, 2)]
    updated = tick_controller.apply_tick(block)
    assert set(updated) == set(block)  # Block should be stable

def test_apply_tick_blinker():
    blinker = [(2, 1), (2, 2), (2, 3)]
    expected_next = [(1, 2), (2, 2), (3, 2)]
    updated = tick_controller.apply_tick(blinker)
    assert set(updated) == set(expected_next)