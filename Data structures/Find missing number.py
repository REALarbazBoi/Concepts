import array

#approach 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 10]
x = range(l[0],l[-1]+1)
missnum = []
for i in x:
    if i not in l:
        missnum.append(i)
print(missnum)


#approach 2

def missing_num(arr):
    s = sum(arr)
    # print(s)
    k = sum(range(arr[0],arr[-1]+1))
    # print(k)
    if k-s>0:
        print("missing number is", k-s)
    else:
        print("There is no number missing")

arr = array.array("i",[2,3,4,5,6,7,8,9,10])

missing_num(arr)



