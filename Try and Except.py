l = [10, 20, 30, 40, 50]

try:
    index = int(input("enter the index number "))
    print(l[index])
    print("end of the try block")
except IndexError:
    print("invalid index")

print("terminated gracefully")


l = [10, 20, 30, 40, 50]

try:
    index = int(input("enter the index number "))
    print(l[index])
    print("end of the try block")
except (IndexError, ValueError)as msg:
    print("invalid index", msg)

print("terminated gracefully")

def division(a,b):
    if b != 0:
        c = a / b
        return c
    else:
        raise ZeroDivisionError


try:
    division(10,20)
except:
    print("zero division error")
