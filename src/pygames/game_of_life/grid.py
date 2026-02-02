from typing import List
from tabulate import tabulate


class Grid:
    def __init__(self, height: int, width: int) -> None:
        self.__height = height
        self.__width = width
        self.__grid = {(i, j): False for i in range(height) for j in range(width)}

    @property
    def grid(self) -> List[List[bool]]:
        return [
            [self.__grid[(i, j)] for j in range(self.__width)]
            for i in range(self.__height)
        ]

    def toggle(self, row: int, col: int) -> None:
        if row >= self.__height or col >= self.__width:
            raise IndexError
        coord = (row, col)
        self.__grid[coord] = not self.__grid[coord]

    def __repr__(self) -> str:
        data = [[int(j) for j in i] for i in self.grid]
        col_indices = ["", *list(range(self.__width))]
        table = tabulate(data, headers=col_indices, showindex="always", tablefmt="grid")
        return str(table)
