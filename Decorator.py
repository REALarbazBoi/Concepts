# def decorator(fun):
#     def wrapper():
#         print("*"*10)
#         fun()
#         print("#"*10)
#     return wrapper
#
# def display():
#     print("hello")
#
# d = decorator(display)
# d()

# def decorator(fun):
#     def wrapper(msg):
#         print("*"*10)
#         fun(msg)
#         print("#"*10)
#     return wrapper
#
# def display(msg):
#     print(msg)
#
# d = decorator(display)
# d("arbaz")

def decorator(fun):
    def wrapper(msg):
        print("*"*10)
        fun(msg)
        print("#"*10)
    return wrapper

@decorator
def display(msg):
    print(msg)

display("arbaz")