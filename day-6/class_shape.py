import math

class Shape:
    def __init__(self,l = None,b = None, h = None, r = None):
        self.l = l
        self.b = b
        self.h = h
        self.r = r

    def Rectangle(self):
        print("Perimeter : {}".format(2*(self.l+self.b)))
        print("Area : {}".format(self.l*self.b))

    def Square(self):
        print("Perimeter : {}".format(4 * self.l))
        print("Area : {}".format(self.l * self.l))

    def Circle(self):
        print("Circumference : {}".format(2*self.r*math.pi))
        print("Area : {}".format(math.pi * pow(self.r,2)))


if __name__=="__main__":
    while True:
        print("""
        1. Rectangle
        2. Square
        3. Curcle
        4. Exit
        """)
        choice = int(input())
        if choice == 1:
            l = int(input("Enter the length : "))
            b = int(input("Enter the breadth : "))
            rec = Shape(l=l,b=b)
            rec.Rectangle()
        elif choice == 2:
            l = int(input("Enter the length : "))
            rec = Shape(l=l)
            rec.Square()
        elif choice == 3:
            r = int(input("Enter the radius : "))
            rec = Shape(r = r)
            rec.Circle()
        else:
            exit()
