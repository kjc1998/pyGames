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

    def test_get_next_iterations(self, interactor: interactor_.Interactor) -> None:
        grid = models.Grid(
            # fmt: off
            [models.Cell(0, 0, False), models.Cell(0, 1, False), models.Cell(0, 2, False), models.Cell(0, 3, False), models.Cell(0, 4, True)],
            [models.Cell(1, 0, False), models.Cell(1, 1, True), models.Cell(1, 2, True), models.Cell(1, 3, False), models.Cell(1, 4, False)],
            [models.Cell(2, 0, False), models.Cell(2, 1, True), models.Cell(2, 2, True), models.Cell(2, 3, False), models.Cell(2, 4, False)],
            [models.Cell(3, 0, False), models.Cell(3, 1, False), models.Cell(3, 2, False), models.Cell(3, 3, False), models.Cell(3, 4, True)],
            [models.Cell(4, 0, True), models.Cell(4, 1, True), models.Cell(4, 2, True), models.Cell(4, 3, False), models.Cell(4, 4, True)],
            # fmt: on
        )
        iteration = models.Iteration(0, grid)
        result = interactor.run_iterations(iteration, 5)
        expected = models.Iteration(
            5,
            models.Grid(
                # fmt: off
            [models.Cell(0, 0, False), models.Cell(0, 1, True), models.Cell(0, 2, True), models.Cell(0, 3, True), models.Cell(0, 4, False)],
            [models.Cell(1, 0, True), models.Cell(1, 1, False), models.Cell(1, 2, False), models.Cell(1, 3, False), models.Cell(1, 4, True)],
            [models.Cell(2, 0, True), models.Cell(2, 1, True), models.Cell(2, 2, False), models.Cell(2, 3, True), models.Cell(2, 4, True)],
            [models.Cell(3, 0, False), models.Cell(3, 1, False), models.Cell(3, 2, False), models.Cell(3, 3, False), models.Cell(3, 4, False)],
            [models.Cell(4, 0, False), models.Cell(4, 1, False), models.Cell(4, 2, False), models.Cell(4, 3, False), models.Cell(4, 4, False)],
                # fmt: on
            ),
        )
        assert len(result) == 5
        assert result[-1] == expected
