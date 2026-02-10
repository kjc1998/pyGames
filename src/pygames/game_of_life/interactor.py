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

    def run_iterations(
        self, iteration: models.Iteration, rounds: int
    ) -> List[models.Iteration]:
        count = 0
        result = []
        while count < rounds:
            iteration = self.__runner.get_next_iteration(iteration)
            result.append(iteration)
            count += 1
        return result
