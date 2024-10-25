import array

ar1 = array.array("i",[10, 20, 30, 40])
print(ar1)

s1 = b'abcde'
ar2 = array.array("b",s1)
print(ar2)
ar2.append(103)
print(ar2)

print(ar2.typecode)