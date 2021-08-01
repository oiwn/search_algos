"""Generate maze"""
import random
import numpy as np


class MazeGen:
    """Generate maze

    TODO: Better maze generation look
    https://en.wikipedia.org/wiki/Maze_generation_algorithm

    NOTE: https://stackoverflow.com/q/38502/1376206
    """

    def __init__(self, dim_x: int, dim_y: int):
        self.dim_x, self.dim_y = dim_x, dim_y

    def generate(self):
        """Generate simple maze, trivial randomized way"""
        arr = np.empty((self.dim_x, self.dim_y), dtype=np.int8)
        select = [0, 0, 0, 0, 0, 3]

        for x in range(self.dim_x):
            for y in range(self.dim_y):
                arr[x][y] = select[random.randint(0, len(select) - 1)]

        # make sure (0, 0) and (dim_x, dim_y) are 0 since it
        # supposed to be enter/exit
        arr[0][0] = 0
        arr[self.dim_x - 1][self.dim_y - 1] = 0

        return arr
