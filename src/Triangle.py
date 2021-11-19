from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, *args, name='triangle'):
        if len(args) != 3:
            raise IndexError('У треугольника должно быть 3 стороны')
        elif (type(args[0]) != int and type(args[0]) != float) or (type(args[1]) != int and type(args[1]) != float) or (
                type(args[2]) != int and type(args[2]) != float):
            raise TypeError('Передано не число')
        elif args[0] <= 0 or args[1] <= 0 or args[2] <= 0:
            raise ValueError('Сторона не может быть равна 0')
        else:
            if args[0] + args[1] > args[2] and args[0] + args[2] > args[1] and args[1] + args[2] > args[0]:
                self.a = args[0]
                self.b = args[1]
                self.c = args[2]
                self.name = name
            else:
                raise ValueError('1 из сторон больше суммы двух других')

    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return (self.perimeter() / 2 * (self.perimeter() / 2 - self.a) * (self.perimeter() / 2 - self.b) * (
                self.perimeter() / 2 - self.c)) ** 0.5
