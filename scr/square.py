from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        if side_a<=0:
            raise ValueError("Сторона квадрата должна быть больше 0")
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4
