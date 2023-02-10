class Shape:
    def __init__(self, length):
        self.length = length


    def area(self):
        print(0)


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        print(self.length ** 2)
       
shape1 = Shape(1)
sq = Square(2)
shape1.area()
sq.area()