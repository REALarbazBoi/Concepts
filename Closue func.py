def closure():
    msg = "hello"
    def display():
        print("*"*10)
        print(msg)
        print(("#"*10))
        return 0
    return display

d = closure()
print(d)
d()

def closure(msg):

    def display():
        print("*"*10)
        print(msg)
        print(("#"*10))
        return 0
    return display

d = closure("Welcome")
# print(d)
d()
