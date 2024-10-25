import bisect


b = [10, 20, 30, 40, 50, 60, 70, 80, 90]
bisect.insort(b, 25)
print(b)
bisect.insort_left(b,90)
print(b)