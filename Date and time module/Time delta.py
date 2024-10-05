import datetime

dt1 = datetime.datetime(2010,10,1,10,20,30)
dt2 = datetime.datetime(2011,10,1,10,20,30)
td = dt2 - dt1
print(td, type(td))
print(dir(td))
print(divmod(td.days,30))

td = datetime.timedelta(31)
dt3 = datetime.datetime.now()
print(dt3+td)
print(dt3 + datetime.timedelta(365))