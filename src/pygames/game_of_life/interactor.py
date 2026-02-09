from pygames.game_of_life import models, runner
from typing import List, Tuple


class Interactor:
    def __init__(self) -> None:
        self.__runner = runner.Runner()

    def build_empty_grid(self, height: int, width: int) -> models.Grid:
        grid = [[models.Cell(i, j, False) for j in range(width)] for i in range(height)]
        return models.Grid(*grid)

    def toggle_grid(self, grid: models.Grid, coords: List[Tuple[int, int]]) -> None:
        for coord in coords:
            row, col = coord
            grid.toggle(row, col)
