import dataclasses
from typing import Any, List
from tabulate import tabulate


@dataclasses.dataclass
class Cell:
    row: int
    col: int
    value: bool

    def __repr__(self) -> str:
        return str(self.value)


class Grid:
    def __init__(self, *rows: List["Cell"]) -> None:
        self.__validate(*rows)
        self.__height = height = len(rows)
        self.__width = width = len(rows[0]) if rows else 0
        self.__rows = list(rows) if height > 0 and width > 0 else []

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    @property
    def rows(self) -> List[List["Cell"]]:
        return [
            [Cell(cell.row, cell.col, cell.value) for cell in row]
            for row in self.__rows
        ]

    def __eq__(self, other: "Any") -> bool:
        if isinstance(other, Grid):
            return self.rows == other.rows
        return False

    def __repr__(self) -> str:
        data = self.__rows
        col_indices = ["", *[str(i) for i in range(self.width)]]
        table = tabulate(data, headers=col_indices, showindex="always", tablefmt="grid")
        return str(table)

    def get_cell(self, row: int, col: int) -> "Cell":
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            raise ValueError("invalid coordinate")
        return self.__rows[row][col]

    def toggle(self, row: int, col: int) -> None:
        cell = self.get_cell(row, col)
        cell.value = not cell.value

    def __validate(self, *rows: List["Cell"]) -> None:
        height, width = len(rows), len(rows[0]) if rows else 0
        coords = [(cell.row, cell.col) for row in rows for cell in row]
        if coords != [(i, j) for i in range(height) for j in range(width)]:
            raise ValueError("invalid cell arrangement")


def build_empty_grid(height: int, width: int) -> "Grid":
    grid = [[Cell(i, j, False) for j in range(width)] for i in range(height)]
    return Grid(*grid)
