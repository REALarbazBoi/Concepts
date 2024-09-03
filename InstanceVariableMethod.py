class Test:

    def __int__(self):
        self.a = 10

    def fun(self):
        self.b = 20

    def aaa(self):
        pass

t1 = Test()
print(t1)
t1.fun()
t1.c = 30
print(dir(t1))
