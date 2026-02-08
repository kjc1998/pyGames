import dataclasses
from pygames.game_of_life import grid as grid_
from typing import List


@dataclasses.dataclass
class Iteration:
    number: int
    grid: grid_.Grid


class Runner:
    def get_next_iteration(self, iteration: "Iteration") -> "Iteration":
        grid = iteration.grid
        new_grid = grid_.Grid(
            *[[grid_.Cell(c.row, c.col, c.value) for c in row] for row in grid.rows]
        )
        self.__update(new_grid)
        return Iteration(iteration.number + 1, new_grid)

    def __update(self, grid: grid_.Grid) -> None:
        def get_neighbours(row: int, col: int) -> List[grid_.Cell]:
            combinations = [
                (i, j) for i in range(row - 1, row + 2) for j in range(col - 1, col + 2)
            ]
            valids = filter(
                lambda c: 0 <= c[0] < grid.height
                and 0 <= c[1] < grid.width
                and c != (row, col),
                combinations,
            )
            return [grid.get_cell(i, j) for i, j in valids]

        for i in range(grid.height):
            for j in range(grid.width):
                cell = grid.get_cell(i, j)
                neighbours = get_neighbours(i, j)
                true_count = [n.value for n in neighbours].count(True)
                if true_count == 3 and not cell.value:  # birth
                    grid.toggle(i, j)
                elif (true_count < 2 or true_count > 3) and cell.value:  # death
                    grid.toggle(i, j)
