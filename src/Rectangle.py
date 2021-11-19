from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, *args, name='rectangle'):
        if len(args) != 2:
            raise IndexError('Должно быть передано только 2 стороны')
        elif type(args[0]) != int and type(args[0]) != float or (type(args[1]) != int and type(args[1]) != float):
            raise TypeError('Передано не число')
        elif args[0] <= 0 or args[1] <= 0:
            raise ValueError('Сторона не может быть меньше или равна 0')
        else:
            self.a = args[0]
            self.b = args[1]
            self.name = name

    def perimeter(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
