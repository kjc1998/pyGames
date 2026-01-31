import pygames
import re


def test_version() -> None:
    expected_pattern = r"^\d+\.\d+\.\d+$"
    observed = pygames.__version__
    assert re.match(expected_pattern, observed)
