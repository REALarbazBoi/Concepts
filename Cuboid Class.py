class cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth

    def total(self):
        return 2* (self.length * self.breadth + self.breadth * self.height + self.height * self.length)

    def volume(self):
        return self.length * self.breadth * self.height

c1 = cuboid(10,5,3)

print(c1.volume())

c2 = cuboid(20,10,5)

print(c1.lidarea())

c3 = cuboid(5,10,15)

print(c3.total())