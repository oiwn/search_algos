"""Generate maze"""
import random
from typing import Tuple

from maze import Maze


class TermColors:
    white = "\033[0m"
    blue = "\033[94m"
    green = "\033[92m"
    red = "\033[91m"
    endc = "\033[0m"


class MazeGen:
    """Generate maze

    TODO: Better maze generation look
    https://en.wikipedia.org/wiki/Maze_generation_algorithm

    NOTE: https://stackoverflow.com/q/38502/1376206
    """

    def __init__(self, shape: Tuple[int, int]):
        self.maze = Maze(shape)
        self.cell = 0
        self.wall = 100
        self.unvisited = -1

    def toggle_wall(self, x: int, y: int, s: str):
        pass

    def make_maze(self):
        """Generate maze"""
        w, h = self.maze.grid.shape
        self.maze.grid.fill(self.unvisited)

        starting_x = random.randint(1, h - 1)
        starting_y = random.randint(1, w - 1)

        self.maze.grid[starting_x][starting_y] = self.cell

        walls = []
        walls.append([starting_x - 1, starting_y])
        walls.append([starting_x, starting_y - 1])
        walls.append([starting_x, starting_y + 1])
        walls.append([starting_x + 1, starting_y])

        self.maze.grid[starting_x - 1][starting_y] = self.wall
        self.maze.grid[starting_x][starting_y - 1] = self.wall
        self.maze.grid[starting_x][starting_y + 1] = self.wall
        self.maze.grid[starting_x + 1][starting_y] = self.wall

        while walls:
            random_wall = random.choice(walls)

        return self.maze

    def generate(self):
        """Generate simple maze, trivial randomized way"""
        select = [0, 0, 0, 0, 0, 255]

        for x in range(self.maze.max_x + 1):
            for y in range(self.maze.max_y + 1):
                self.maze.grid[x][y] = select[
                    random.randint(0, len(select) - 1)
                ]

        # make sure (0, 0) and (max_x, max_y) are 0 since it
        # supposed to be enter/exit
        self.maze.grid[0][0] = 0
        self.maze.grid[self.maze.max_x][self.maze.max_y] = 0

        return self.maze

    def print_maze(self):
        """Print maze to the console"""
        height, width = self.maze.grid.shape
        for i in range(0, height):
            for j in range(0, width):
                if self.maze.grid[i][j] == self.unvisited:
                    print(TermColors.white + "u" + TermColors.endc, end=" ")
                elif self.maze.grid[i][j] == self.cell:
                    print(TermColors.green + "c" + TermColors.endc, end=" ")
                else:
                    print(TermColors.red + "w" + TermColors.endc, end=" ")

            print("\n")
