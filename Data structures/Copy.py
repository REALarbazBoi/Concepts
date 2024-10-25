import copy


# l = [10, 20, 30, 40]
# l1 = copy.copy(l)
# print(l1)
# print(id(l))
# print(id(l1))
# print(id(l[0]))
# print(id(l1[0]))
# l[1] = 5
# print(l)
# print(l1)

class Person:
    def __init__(self,name):
        self.name = name

l = [Person("Arbaz"), Person("Noor"), Person("Vikesh")]
l1 = copy.deepcopy(l)
print(id(l[0]))
print(id(l1[0]))