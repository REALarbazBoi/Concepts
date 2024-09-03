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

    @staticmethod
    def issquare(len, bre):
        return len == bre

r1 = Rectangle(10, 5)
print(r1.issquare(10,5))
