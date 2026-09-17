from math import sqrt

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("Сумма двух любых сторон должна быть больше третьей")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.__p = None

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        self.__p = self.perimeter / 2
        return round(sqrt(self.__p * (self.__p - self.side_a) * \
                    (self.__p - self.side_b) * (self.__p - self.side_c)), 4)
