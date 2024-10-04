import datetime

dt1 = datetime.datetime(2002,12,25,16,15,14)
dt2 = datetime.datetime(year=2004, month=12, day=20, hour=23, minute=15, second=59)
print(dt2 - dt1)
print(dt1 > dt2)

dat1 = datetime.date(2015, 12, 4)
tim1 = datetime.time(17, 18, 19)
dt3 = datetime.datetime.combine(dat1 ,tim1)
print(dt3)

dat1 = datetime.date(2015,11,11)
dat2 = datetime.date(2016,11,11)
print(dat2 - dat1)
print(dat2 > dat1)
tim1 = datetime.time(23,23,23)
tim2 = datetime.time(22,22,22)
# print(tim2 - tim1) # cannot sub time
print(tim2 > tim1)

dt2 = datetime.datetime(year=2004, month=12, day=20, hour=23, minute=15, second=59)
dt3 = datetime.datetime.now()
print(dt3 - dt2)