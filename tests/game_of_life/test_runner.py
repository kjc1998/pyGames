import pytest
from pygames.game_of_life.models import *
from pygames.game_of_life import runner as runner_


class TestRunner:
    @pytest.fixture
    def iteration(self) -> Iteration:
        """
        Return iteration with following grid layout:

        |  |0 |1 |2 |3 |4 |
        | 0|  |  |  |  |X |
        | 1|  |X |X |  |  |
        | 2|  |X |X |  |  |
        | 3|  |  |  |  |X |
        | 4|X |X |X |  |X |
        """
        grid = Grid(
            # fmt: off
            [Cell(0, 0, False), Cell(0, 1, False), Cell(0, 2, False), Cell(0, 3, False), Cell(0, 4, True)],
            [Cell(1, 0, False), Cell(1, 1, True), Cell(1, 2, True), Cell(1, 3, False), Cell(1, 4, False)],
            [Cell(2, 0, False), Cell(2, 1, True), Cell(2, 2, True), Cell(2, 3, False), Cell(2, 4, False)],
            [Cell(3, 0, False), Cell(3, 1, False), Cell(3, 2, False), Cell(3, 3, False), Cell(3, 4, True)],
            [Cell(4, 0, True), Cell(4, 1, True), Cell(4, 2, True), Cell(4, 3, False), Cell(4, 4, True)],
            # fmt: on
        )
        return Iteration(0, grid)

    def test_get_next_iteration(self, iteration: Iteration) -> None:
        runner = runner_.Runner()
        observed = runner.get_next_iteration(iteration)
        expected = Iteration(
            1,
            Grid(
                # fmt: off
                [Cell(0, 0, False), Cell(0, 1, False), Cell(0, 2, False), Cell(0, 3, False), Cell(0, 4, False)],
                [Cell(1, 0, False), Cell(1, 1, True), Cell(1, 2, True), Cell(1, 3, True), Cell(1, 4, False)],
                [Cell(2, 0, False), Cell(2, 1, True), Cell(2, 2, True), Cell(2, 3, True), Cell(2, 4, False)],
                [Cell(3, 0, True), Cell(3, 1, False), Cell(3, 2, False), Cell(3, 3, False), Cell(3, 4, False)],
                [Cell(4, 0, False), Cell(4, 1, True), Cell(4, 2, False), Cell(4, 3, True), Cell(4, 4, False)],
                # fmt: on
            ),
        )
        assert observed == expected
