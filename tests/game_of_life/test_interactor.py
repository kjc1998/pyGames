import pytest
from pygames.game_of_life import models, interactor as interactor_


class TestInteractor:
    @pytest.fixture
    def interactor(self) -> interactor_.Interactor:
        return interactor_.Interactor()

    def test_build_empty_grid(self, interactor: interactor_.Interactor) -> None:
        grid = interactor.build_empty_grid(5, 6)
        assert grid.height == 5
        assert grid.width == 6

    def test_toggle_grid(self, interactor: interactor_.Interactor) -> None:
        grid = interactor.build_empty_grid(2, 2)
        assert grid == models.Grid(
            [models.Cell(0, 0, False), models.Cell(0, 1, False)],
            [models.Cell(1, 0, False), models.Cell(1, 1, False)],
        )
        interactor.toggle_grid(grid, [(0, 0), (1, 1)])
        expected = models.Grid(
            [models.Cell(0, 0, True), models.Cell(0, 1, False)],
            [models.Cell(1, 0, False), models.Cell(1, 1, True)],
        )
        assert grid == expected
