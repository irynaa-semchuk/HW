import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(3, 9) == 12
    assert Calculator.add(2, 9) == 11
    assert Calculator.add(0.5, 12) == 12.5
    with pytest.raises(TypeError):
        Calculator.add([1,2], 2)


def test_subtract():
    assert Calculator.subtract(9, 8) == 1
    assert Calculator.subtract(9, 7) == 2
    assert Calculator.subtract(9.1, 1) == 8.1
    with pytest.raises(TypeError):
        Calculator.subtract([1,4], 2)


def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(2, 9) == 18
    assert Calculator.multiply(3, 4) == 12
    with pytest.raises(TypeError):
        Calculator.multiply([1,5], 2)


def test_divide():
    assert Calculator.divide(2, 6) == 3
    assert Calculator.divide(2, 12) == 6
    assert Calculator.divide(2, 18) == 9
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)

