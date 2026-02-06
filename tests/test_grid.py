import pytest
from pygames.game_of_life.grid import *


class TestGrid:
    @pytest.fixture
    def grid(self) -> Grid:
        return build_empty_grid(3, 2)

    def test_grid_initialisation(self) -> None:
        Grid()
        Grid(
            [Cell((0, 0), False), Cell((0, 1), True)],
            [Cell((1, 0), True), Cell((1, 1), False)],
        )

    def test_validate(self) -> None:
        with pytest.raises(ValueError):
            # inconsistent column count
            Grid(
                [Cell((0, 0), False), Cell((0, 1), True)],
                [Cell((1, 0), False)],
            )
        with pytest.raises(ValueError):
            # invalid column arrangement
            Grid(
                [Cell((0, 0), False), Cell((0, 1), True)],
                [Cell((1, 1), False), Cell((1, 0), True)],
            )
        with pytest.raises(ValueError):
            # invalid row arrangement
            Grid(
                [Cell((1, 0), True), Cell((1, 1), False)],
                [Cell((0, 0), False), Cell((0, 1), True)],
            )

    def test_properties(self, grid: Grid) -> None:
        assert grid.height == 3
        assert grid.width == 2
        assert grid.grid == [
            [Cell((0, 0), False), Cell((0, 1), False)],
            [Cell((1, 0), False), Cell((1, 1), False)],
            [Cell((2, 0), False), Cell((2, 1), False)],
        ]

    def test_empty_grid(self) -> None:
        empty_grid = Grid()
        assert empty_grid == Grid() == Grid([])
        assert empty_grid.height == empty_grid.width == 0

    def test_grid(self, grid: Grid) -> None:
        expected = Grid(
            [Cell((0, 0), False), Cell((0, 1), False)],
            [Cell((1, 0), False), Cell((1, 1), False)],
            [Cell((2, 0), False), Cell((2, 1), False)],
        )
        assert grid == expected

    def test_toggle(self, grid: Grid) -> None:
        grid.toggle(2, 0)
        assert grid == Grid(
            [Cell((0, 0), False), Cell((0, 1), False)],
            [Cell((1, 0), False), Cell((1, 1), False)],
            [Cell((2, 0), True), Cell((2, 1), False)],
        )

    def test_toggle_error(self, grid: Grid) -> None:
        with pytest.raises(ValueError):
            grid.toggle(3, 0)
