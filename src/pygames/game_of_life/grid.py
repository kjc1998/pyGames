import dataclasses
from typing import Any, List, Tuple
from tabulate import tabulate


@dataclasses.dataclass
class Cell:
    coord: Tuple[int, int]
    value: bool

    def __repr__(self) -> str:
        return str(self.value)


class Grid:
    def __init__(self, *rows: List["Cell"]) -> None:
        self.__validate(*rows)
        self.__height = height = len(rows)
        self.__width = width = len(rows[0]) if rows else 0
        self.__grid = list(rows) if height > 0 and width > 0 else []

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def grid(self) -> List[List["Cell"]]:
        return [[Cell(cell.coord, cell.value) for cell in row] for row in self.__grid]

    def __eq__(self, other: "Any") -> bool:
        if isinstance(other, Grid):
            return self.grid == other.grid
        return False

    def __repr__(self) -> str:
        data = self.__grid
        col_indices = ["", *list(range(self.width))]
        table = tabulate(data, headers=col_indices, showindex="always", tablefmt="grid")
        return str(table)

    def toggle(self, row: int, col: int) -> None:
        if row >= self.height or col >= self.width:
            raise ValueError("invalid coordinate")
        cell = self.__grid[row][col]
        cell.value = not cell.value

    def __validate(self, *rows: List["Cell"]) -> None:
        height, width = len(rows), len(rows[0]) if rows else 0
        coords = [cell.coord for row in rows for cell in row]
        if coords != [(i, j) for i in range(height) for j in range(width)]:
            raise ValueError("invalid cell arrangement")


def build_empty_grid(height: int, width: int) -> "Grid":
    grid = [[Cell((i, j), False) for j in range(width)] for i in range(height)]
    return Grid(*grid)
