from .utils import my_mean


def test_long():
    assert my_mean([1, 2, 3]) == 2


def test_short():
    assert my_mean([1, 2]) == 1.5


def test_single():
    assert my_mean([1]) == 1


def test_empty():
    assert my_mean([]) == 0
