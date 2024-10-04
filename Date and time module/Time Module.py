import datetime
import time

print(time.time())
print(time.localtime())
lt = time.localtime()
print(type(lt))
print(time.localtime().tm_hour)
print(lt.tm_mday)
print(lt.tm_min)
print(lt.tm_sec)
print(lt.tm_wday)  # zero is monday
p = time.ctime()
print(type(p))
print(datetime.datetime.now())
dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.minute)
dt = datetime.datetime.today()
print(dt)