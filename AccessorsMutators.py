class Rectangle:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def getlength(self):
        return self.length

    def getbreadth(self):
        return self.breadth

    def setlength(self,l):
        self.length = l

    def setbreadth(self, b):
        self.breadth = b

r1 = Rectangle(10,5)
print(r1.getlength())
print(r1.getbreadth())
r1.setlength(20)
r1.setbreadth(30)
print(r1.getlength())
print(r1.getbreadth())