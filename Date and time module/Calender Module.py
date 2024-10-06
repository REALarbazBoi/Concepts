from calendar import *

print(firstweekday())
print(isleap(2005))
print(leapdays(2004,2024))
print(weekday(2024, 11, 3))
prmonth(2024,10)


c = Calendar()
for i in c.iterweekdays():
    print(i)

for i in c.itermonthdates(2024, 10):
    print(i)

for i in c.itermonthdays(2024, 10):
    print(i)

print(weekday(2024, 9, 30))

for i in c.itermonthdays4(2024, 10):
    print(i)

print(c.monthdatescalendar(2024, 10))

c = TextCalendar()

c.prmonth(2023,10)

c.pryear(2024)

print(c.formatmonth(2024, 10))

c = HTMLCalendar()

print(c.formatmonth(2024, 10))