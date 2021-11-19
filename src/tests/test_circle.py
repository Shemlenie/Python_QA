import pytest
from src.Figure import Figure
from src.Circle import Circle
from src.Square import Square


@pytest.mark.parametrize('a', [
    (10),
    (10.5),
    ('asd'),
    (0),
    (-10),
    ()
])
def test_circle_create(a):
    try:
        circle = Circle(a)
    except Exception:
        assert 1
        return
    assert issubclass(type(circle), Figure)

def test_circle_create_2():
    try:
        Circle(10, 10)
    except IndexError:
        assert 1
        return
    assert 0

def test_circle_create_0():
    try:
        Circle()
    except IndexError:
        assert 1
        return
    assert 0

def test_circle_area():
    assert Circle(10).area == 314

def test_circle_perimeter():
    assert Circle(10).perimeter() == 2 * 10 * 3.14

def test_add_area_1():
    circle = Circle(10)
    square = Square(10)
    assert circle.add_area(square) == 414

def test_add_area_2():
    try:
        circle = Circle(10)
        square = Square(10, 10)
        circle.add_area(square)
    except IndexError:
        assert 1
        return
    assert 0
