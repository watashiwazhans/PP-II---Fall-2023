class Rectange(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        print(self.length * self.width)


rect = Rectange(2,3)
rect.area()