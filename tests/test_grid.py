import pytest
from pygames.game_of_life import grid as grid_


class TestGrid:
    @pytest.fixture
    def grid(self) -> grid_.Grid:
        return grid_.Grid(3, 2)

    def test_grid(self, grid: grid_.Grid) -> None:
        expected = [[False, False], [False, False], [False, False]]
        assert grid.grid == expected

    def test_toggle(self, grid: grid_.Grid) -> None:
        grid.toggle(1, 1)
        grid.toggle(0, 0)
        assert grid.grid == [[True, False], [False, True], [False, False]]
        grid.toggle(1, 1)
        assert grid.grid == [[True, False], [False, False], [False, False]]

        with pytest.raises(IndexError):
            grid.toggle(1, 3)
