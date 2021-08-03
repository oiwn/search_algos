"""Generate maze"""
import random
from typing import Tuple

from maze import Maze


class MazeGen:
    """Generate maze

    TODO: Better maze generation look
    https://en.wikipedia.org/wiki/Maze_generation_algorithm

    NOTE: https://stackoverflow.com/q/38502/1376206
    """

    def __init__(self, shape: Tuple[int, int]):
        self.maze = Maze(shape)

    def generate(self):
        """Generate simple maze, trivial randomized way"""
        select = [0, 0, 0, 0, 0, 255]

        for x in range(self.maze.max_x):
            for y in range(self.maze.max_y):
                self.maze.grid[x][y] = select[
                    random.randint(0, len(select) - 1)
                ]

        # make sure (0, 0) and (max_x, max_y) are 0 since it
        # supposed to be enter/exit
        self.maze.grid[0][0] = 0
        self.maze.grid[self.maze.max_x][self.maze.max_y] = 0

        return self.maze
