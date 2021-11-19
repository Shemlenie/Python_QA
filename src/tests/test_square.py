import pytest
from src.Figure import Figure
from src.Triangle import Triangle
from src.Square import Square


@pytest.mark.parametrize('a', [
    (10),
    (10.5),
    ('asd'),
    (0),
    (-10),
    ()
])
def test_square_create(a):
    try:
        square = Square(a)
    except Exception:
        assert 1
        return
    assert issubclass(type(square), Figure)

def test_square_create_2():
    try:
        Square(10, 10)
    except IndexError:
        assert 1
        return
    assert 0

def test_square_create_0():
    try:
        Square()
    except IndexError:
        assert 1
        return
    assert 0

def test_square_area():
    assert Square(10).area == 100

def test_square_perimeter():
    assert Square(10).perimeter() == 40

def test_add_area_1():
    square = Square(10)
    triangle = Triangle(13, 14, 15)
    assert square.add_area(triangle) == 184

def test_add_area_2():
    try:
        square = Square(10)
        triangle = Triangle(13, 14, 15, 16)
        square.add_area(triangle)
    except IndexError:
        assert 1
        return
    assert 0
