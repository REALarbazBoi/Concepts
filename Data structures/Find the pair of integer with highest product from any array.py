#Find the pair of integer with highest product from any array

import array


def max_prod(arr):
    d = {}
    for i in range(len(arr)):
        for j in range(len(arr)):
            d[arr[i] * arr[j]] = arr[i], arr[j]
    return (d[max(d.keys())])


arr=array.array("i",[2, 3, 6, 4, 8, 7, 9])
print(max_prod(arr))


def max_prod(arr): # correct approach
    x = arr[0]
    y = arr[1]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > x * y:
                x = arr[i]
                y = arr[j]
    return x, y

arr=array.array("i",[2, 3, 6, 4, 8, 7, 9])

print(max_prod(arr))
