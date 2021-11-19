import pytest
from src.Figure import Figure
from src.Triangle import Triangle
from src.Square import Square


@pytest.mark.parametrize('a, b, c', [
    (13, 14, 15),
    (13.2, 15.3, 14.4),
    (13, 'asd', 15),
    (13, 100000, 13),
    (0, 12, 13),
    (-10, 11, 12)
])
def test_triangle_create_3(a, b, c):
    try:
        triangle = Triangle(a, b, c)
    except Exception:
        assert 1
        return
    assert issubclass(type(triangle), Figure)

def test_triangle_create_4():
    try:
        Triangle(13, 14, 15, 16)
    except IndexError:
        assert 1
        return
    assert 0

def test_triangle_create_2():
    try:
        Triangle(13, 14)
    except IndexError:
        assert 1
        return
    assert 0

def test_triangle_area():
    assert Triangle(13, 14, 15).area == 84

def test_triangle_perimeter():
    assert Triangle(13, 14, 15).perimeter() == 42

def test_add_area_1():
    square = Square(10)
    triangle = Triangle(13, 14, 15)
    assert triangle.add_area(square) == 184

def test_add_area_2():
    try:
        square = Square(10, 10)
        triangle = Triangle(13, 14, 15)
        triangle.add_area(square)
    except IndexError:
        assert 1
        return
    assert 0
