"""A*-search algo
https://en.wikipedia.org/wiki/A*_search_algorithm
"""
# pylint: disable=missing-function-docstring
import heapq
from typing import List, Tuple, Dict, TypeVar, Optional


T = TypeVar("T")
Point = Tuple[int, int]


class PriorityQueue:
    """Queue with priorities"""

    def __init__(self):
        self.elements: List[Tuple[int, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


class AStarSearch:
    """Implementation of A*-search algorithm"""

    def __init__(self, maze, start: Point, stop: Point):
        """Init maze"""
        self.maze = maze
        self.start = start
        self.stop = stop

    @staticmethod
    def heuristic(a: Point, b: Point) -> int:
        x_1, y_1 = a
        x_2, y_2 = b
        return abs(x_1 - x_2) + abs(y_1 - y_2)

    def run(self):
        open_vertixes = PriorityQueue()
        open_vertixes.put(self.start, 0)

        came_from: Dict[Point, Optional[Point]] = {}
        cost_so_far: Dict[Point, int] = {}
        came_from[self.start] = None
        cost_so_far[self.start] = 0

        while not open_vertixes.empty():
            current = open_vertixes.get()
            if current == self.stop:
                break

            for point in self.maze.get_cell_neighbors(current):
                new_cost = cost_so_far[current] + self.heuristic(
                    point, self.stop
                )
                if point not in cost_so_far or new_cost < cost_so_far[point]:
                    cost_so_far[point] = new_cost
                    priority = new_cost + self.heuristic(point, self.stop)
                    open_vertixes.put(point, priority)
                    came_from[point] = current

        return came_from, cost_so_far

    def reconstruct_path(self, came_from: Dict[Point, Point]) -> List[Point]:
        current: Point = self.stop
        path: List[Point] = []
        while current != self.start:
            path.append(current)
            try:
                current = came_from[current]
            except KeyError:
                # sometimes got blocked due to shit maze generation
                print(came_from)
                break
        path.append(self.start)
        path.reverse()
        return path
