import dataclasses
from pygames.game_of_life import models
from typing import List


class Runner:
    def get_next_iteration(self, iteration: models.Iteration) -> models.Iteration:
        grid = iteration.grid
        new_grid = self.__build_new_grid(grid)
        return models.Iteration(iteration.number + 1, new_grid)

    def __build_new_grid(self, grid: models.Grid) -> models.Grid:
        height, width = grid.height, grid.width

        def get_neighbours(row: int, col: int) -> List[models.Cell]:
            combinations = [
                (i, j) for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)
            ]
            valids = filter(
                lambda c: 0 <= c[0] < height and 0 <= c[1] < width and c != (row, col),
                combinations,
            )
            return [grid.get_cell(i, j) for i, j in valids]

        new_grid = models.Grid(
            *[[models.Cell(c.row, c.col, c.value) for c in row] for row in grid.rows]
        )
        for i in range(height):
            for j in range(width):
                cell = new_grid.get_cell(i, j)
                neighbours = get_neighbours(i, j)
                true_count = [n.value for n in neighbours].count(True)
                if true_count == 3 and not cell.value:  # birth
                    new_grid.toggle(i, j)
                elif (true_count < 2 or true_count > 3) and cell.value:  # death
                    new_grid.toggle(i, j)
        return new_grid
