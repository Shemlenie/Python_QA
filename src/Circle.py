from src.Figure import Figure


class Circle(Figure):

    def __init__(self, *args, name='circle'):
        if len(args) != 1:
            raise IndexError('Должен быть передан только радиус')
        elif type(args[0]) != int and type(args[0]) != float:
            raise TypeError('Передано не число')
        elif args[0] <= 0:
            raise ValueError('Радиус не может быть меньше или равен 0')
        else:
            self.r = args[0]
            self.name = name

    def perimeter(self):
        return 2 * self.r * 3.14

    @property
    def area(self):
        return self.r ** 2 * 3.14
