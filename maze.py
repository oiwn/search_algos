"""Support maze data structure and common operations ower it"""
from typing import Tuple, List, Iterator

import numpy as np


Point = Tuple[int, int]


class Maze:
    """Maze data strucuture with common operations

    Maze represented as numpy array, where cell is wall if it value > 0
    """

    def __init__(self, shape: Tuple[int, int]):
        self.grid = np.zeros(shape, dtype=np.int16)
        self.max_x = shape[0] - 1
        self.max_y = shape[1] - 1

    def get_cell_neighbors(self, cell: Point) -> Iterator[Point]:
        """Get NESW points coordinates if present"""
        x, y = cell
        #  neighbors = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        if (x + y) % 2 == 0:
            neighbors.reverse()
        for point in neighbors:
            p_x, p_y = point
            if (0 <= p_x <= self.max_x) and (0 <= p_y <= self.max_y):
                if self.grid[p_x][p_y] == 0:
                    yield point
