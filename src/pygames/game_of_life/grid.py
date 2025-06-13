from typing import List, Dict, Tuple


def get_next_status(current: bool, neighbours: List[bool]) -> bool:
    maintain = current and len(neighbours) == 2
    reproduction = len(neighbours) == 3
    return maintain or reproduction


class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__grid = {(i, j): False for i in range(height) for j in range(width)}

    def set_active(self, row: int, column: int) -> None:
        if row >= self.__width or column >= self.__height:
            raise ValueError

    def next_iteration(self) -> "Grid":
        next_grid = Grid()
        return next_grid
