class Shape:
    def __init__(self , l = None , b = None , h = None , r = None):
        self.l = l
        self.b = b
        self.h = h
        self.r = r

    def area(self):
        print("This is a parent class")
        pass
    def perimeter(self):
        pass


class Rectangle(Shape):

    # def area(self):
    #     print("Area : {}".format(self.l*self.b))

    def perimeter(self):
        print("Perimeter : {}".format(2*(self.l+self.b)))


class Square(Shape):
    def area(self):
        print("Area : {}".format(self.l*self.l))

    def perimeter(self):
        print("Perimeter : {}".format(4*self.l))

shapes = [Rectangle(5,5), Square(10)]

for shape in shapes:
    shape.area()
    shape.perimeter()