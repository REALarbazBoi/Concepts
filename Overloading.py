class Arith:
    def sum(self,a,b,c=None):
        s = a + b
        if c==None:
            return s
        else:
            return c+s


a = Arith()
print(a.sum(5,10,15))
print(a.sum(10.5,16.1))
print(a.sum("hello ","world"))