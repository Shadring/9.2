import pytest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('Деление на ноль невозможно')
    return x / y


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(0, 0) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
