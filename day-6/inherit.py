"""
Inheritence
"""
import math


class Shape:
    def __init__(self,l = None,b = None, h = None, r = None):
        self.l = l
        self.b = b
        self.h = h
        self.r = r

    def sides(self):
        count = 0
        if self.l:
            count += 1
        if self.b:
            count += 1
        if self.r:
            print("No sides")
            return 0
        print("Sides : {}".format(count))


class Rectangle(Shape):
    def __init__(self,l,b):
        super().__init__(l=l,b=b)
        # self.l = l
        # self.b = b

    def area(self):
        print("Area : {}".format(self.l*self.b))

    def perimeter(self):
        print("Perimeter : {}".format(2 *(self.l+self.b)))


class Circle(Shape):
    def area(self):
        print("Area : {}".format(math.pi*pow(self.r,2)))


a = Rectangle(4,5)
a.sides()
a.area()
a.perimeter()

print("CIRCLE")
c = Circle(r=10)
c.area()
c.sides()