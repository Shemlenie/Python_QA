from src.Figure import Figure


class Square(Figure):

    def __init__(self, *args, name='square'):
        if len(args) != 1:
            raise IndexError('Должна быть передана только 1 сторона')
        elif type(args[0]) != int and type(args[0]) != float:
            raise TypeError('Передано не число')
        elif args[0] <= 0:
            raise ValueError('Сторона не может быть меньше или равна 0')
        else:
            self.a = args[0]
            self.name = name

    def perimeter(self):
        return self.a * 4

    @property
    def area(self):
        return self.a ** 2
