import math


class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("Area : {}".format(self.l * self.b))

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        print("Area : {}".format(self.r*self.r* math.pi))


a = [Rectangle(5,6), Circle(10)]

for i in a:
    i.area()

