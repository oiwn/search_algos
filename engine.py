"""Visualization of pathfinding"""
import pygame
from maze_gen import MazeGen
from a_search import AStarSearch


class Engine:  # pylint: disable=too-few-public-methods
    """Main engine"""

    def __init__(self):
        """Initialize engine"""

        pygame.init()
        self.display = pygame.display.set_mode((640, 480), flags=pygame.SCALED)
        self.maze = MazeGen((70, 60)).generate()

        search = AStarSearch(self.maze, (0, 0), (69, 59))
        came_from, _ = search.run()
        path = search.reconstruct_path(came_from)
        for x, y in path:
            self.maze.grid[x][y] = 100

        self.surface = pygame.surfarray.make_surface(self.maze.grid)

    def loop(self):
        """Main loop"""
        running: bool = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    running = False

            self.display.blit(
                pygame.transform.scale(self.surface, (640, 480)), (0, 0)
            )
            pygame.display.flip()

        pygame.quit()
