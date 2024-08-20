#win1
f= open("Python1.jpeg","rb")

data = f.read()

cp= open("Python2.jpeg", "wb")

cp.write(data)

f.close()
cp.close()

#win2
with open("my.data", "wb") as f:
    f.write(b"abcdefghij")

#win3
with open("my.data","rb") as f:
    print(f.read(2).decode())
    f.seek(3,0)
    print(f.read(1).decode())
    f.seek(3,1)
    print(f.read(1).decode())
    f.seek(-3,2)
    print(f.read(1).decode())
    print(f.tell())
