import pytest
from src.lib import get_stepping_variants


def f():
    return 1


def g():
    return 2


def h():
    return 3


@pytest.fixture
def consecutive_calls():
    def i():
        return f() + g() + h()

    return i.__code__


def test_candidates_for_consecutive_calls(consecutive_calls):
    variants = list(get_stepping_variants(consecutive_calls))
    assert len(variants) == 5
    assert variants[0].argval == 'f'
    assert variants[1].argval == 'g'
    assert variants[2].argval == '__add__'
    assert variants[3].argval == 'h'
    assert variants[4].argval == '__add__'
