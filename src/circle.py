from math import pi

from src.figure import Figure


class Circle(Figure):
    def __init__(self, rad):
        if rad<=0 :
            raise ValueError("Радиус круга должен быть больше 0")
        self.rad = rad

    @property
    def perimeter(self):
        return round(2 * pi * self.rad, 4)

    @property
    def area(self):
        return round(pi * (self.rad ** 2), 4)
