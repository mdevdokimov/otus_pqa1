from math import pi
from figure import Figure

class Circle(Figure):
    def __init__(self, rad):
        if rad<=0 :
            raise ValueError("Радиус круга должен быть больше 0")
        self.rad = rad

    @property
    def perimeter(self):
        return 2 * pi * self.rad

    @property
    def area(self):
        return pi * (self.rad ** 2)
