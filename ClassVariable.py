class Rectangle:
    count = 0

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count += 1
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    @classmethod
    def countRect(cls):
        print(cls.count)

r1 =Rectangle(10,5)

r1.countRect()

r2 = Rectangle(7,10)
r2.countRect()
Rectangle.countRect()
