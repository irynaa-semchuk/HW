import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(3, 9) == 12
    assert Calculator.add(2, 9) == 11
    assert Calculator.add(0.5, 12) == 12.5


def test_add_negative_case():
    with pytest.raises(TypeError):
        Calculator.add([1, 2], 2)
        Calculator.add('3', 8)
        Calculator.add((2, 8), 8)


def test_subtract():
    assert Calculator.subtract(9, 8) == 1
    assert Calculator.subtract(9, 7) == 2
    assert Calculator.subtract(9.1, 1) == 8.1


def test_subtract_negative_case():
    with pytest.raises(TypeError):
        Calculator.subtract([1, 4], 2)
        Calculator.subtract(None, 8)
        Calculator.subtract('9', (9, 6))


def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(2, 9) == 18
    assert Calculator.multiply(3, 4) == 12


def test_multiply_negative_case():
    with pytest.raises(TypeError):
        Calculator.multiply(None, 2)
        Calculator.multiply('8', [1, 2])
        Calculator.multiply([0, 8], {0, 8})



def test_divide():
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(12, 2) == 6
    assert Calculator.divide(18, 2) == 9


def test_divide_negative_case():
    with pytest.raises(TypeError):
        Calculator.divide(None, 2)
        Calculator.divide((9, 9), 7)
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
        Calculator.divide(-1, 0)
        Calculator.divide(1.9, 0)

