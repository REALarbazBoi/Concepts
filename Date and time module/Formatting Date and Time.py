import datetime

dt1 = datetime.datetime(2010, 1, 1, 10, 20, 30)
print(dt1)
print(dt1.strftime("%d %B, %A %Y. %H:%M:%S "))


str1 = "10 Jan 2015, 10:30:50"
print(type(str1))
dt2 = datetime.datetime.strptime(str1, "%d %b %Y, %H:%M:%S")
print(dt2)
print(type(dt2))