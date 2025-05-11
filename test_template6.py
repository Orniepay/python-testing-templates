# NOTE:
# How to run:
# pip install pytest
# pip install pytest pytest-sugar
# python -m pytest test_template6.py

# test_calculator_pytest.py
from calculator import square

def test_square_2():
    assert square(2) == 4

def test_square_3():
    assert square(3) == 9

def test_square_4():
    assert square(4) == 16

def test_square_5():
    assert square(5) == 25

def test_square_6():
    assert square(6) == 36
