from abc import ABC, abstractmethod

class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if issubclass(type(figure), Figure):
            return self.area + figure.area
        else:
            raise ValueError('Передан неправильный класс')


