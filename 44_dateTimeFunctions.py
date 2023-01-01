import datetime as dt

a = dt.date.today()
print(a)

date = dt.date(2021, 12, 29)
print(date)
print('Year', date.year)
print('month', date.month)
print('Date', date.day)

time = dt.time(4,45,45,45555)
print(time)
print('Hours: ', time.hour)
print('Minutes: ', time.minute)
print('Seconds: ', time.second)
print('MiCROSECONDS: ', time.microsecond)

dayAndTime = dt.datetime.now()
print(dayAndTime)

newDt = dt.datetime(2022, 12, 20, 5, 45, 40, 44)
print(newDt.date())
print(newDt.time())

current  = dt.datetime.now()
s = current
print(s.strftime('%A %B %d %y'))