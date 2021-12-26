import random
from dataclasses import dataclass
from enum import Enum
from typing import List, NamedTuple


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


@dataclass
class Maze:
    rows: int = 10
    columns: int = 10
    sparseness: float = 0.2
    start: MazeLocation = MazeLocation(0, 0)
    goal: MazeLocation = MazeLocation(9, 9)

    def __post_init__(self):
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for _ in range(self.columns)] for _ in range(self.rows)
        ]
        self._randomize()
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def _randomize(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if random.uniform(0, 1.0) < self.sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        return "".join(["".join([c.value for c in row]) + "\n" for row in self._grid])


if __name__ == "__main__":
    maze = Maze()
    print(maze)
