import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.mark.parametrize('a, b', [
    (10, 15),
    (10.5, 10),
    (10, 'asd'),
    (0, 10),
    (-10, 10)
])
def test_rectangle_create(a, b):
    try:
        rectangle = Rectangle(a)
    except Exception:
        assert 1
        return
    assert issubclass(type(rectangle), Figure)

def test_rectangle_create_3():
    try:
        Rectangle(10, 11, 12)
    except IndexError:
        assert 1
        return
    assert 0

def test_rectangle_create_1():
    try:
        Rectangle(10)
    except IndexError:
        assert 1
        return
    assert 0

def test_rectangle_area():
    assert Rectangle(10, 15).area == 150

def test_rectangle_perimeter():
    assert Rectangle(10, 15).perimeter() == 50

def test_add_area_1():
    rectangle = Rectangle(10, 15)
    square = Square(10)
    assert rectangle.add_area(square) == 250

def test_add_area_2():
    try:
        rectangle = Rectangle(10, 15)
        square = Square(10, 10)
        rectangle.add_area(square)
    except IndexError:
        assert 1
        return
    assert 0
