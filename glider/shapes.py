import numpy as np

def shape():
    return np.random.randint(0, 2, size=(10, 10)).tolist()

def block():
    return [
        [1, 1],
        [1, 1]
    ]

def blinker():
    return [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

def glider():
    return [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]

def glider_plus():
    return [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

def beacon():
    return [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

def toad():
    return [
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ]

def pulsar():
    return [
        [0,0,1,1,1,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,0,0,0,1,0,1,0,0,0,0,1],
        [0,0,1,1,1,0,0,0,1,1,1,0,0]
    ]

def shapeCube(size, offset=(0, 0, 0)):
    ox, oy, oz = offset
    # A 3D block: 2x2x2 cube
    return [
        (ox + x, oy + y, oz + z)
        for x in range(size)
        for y in range(size)
        for z in range(size)
    ]