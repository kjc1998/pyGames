import pytest
from pygames.game_of_life import cell


class TestCell:
    @pytest.fixture
    def a_cell(self) -> cell.Cell:
        return cell.Cell()

    def test_default_is_alive(self, a_cell: cell.Cell):
        assert a_cell.is_alive == False

    def test_switch(self, a_cell: cell.Cell):
        assert a_cell.is_alive == False
        a_cell.switch()
        assert a_cell.is_alive == True
        a_cell.switch()
        assert a_cell.is_alive == False
