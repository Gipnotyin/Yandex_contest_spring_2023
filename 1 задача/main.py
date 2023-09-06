from datetime import datetime, time
from calendar import isleap


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def year(start: datetime, end: datetime, days):
    for i in range(start.year, end.year):
        if isleap(i):
            days -= 1
    return days


def count_days(year, month, day):
    count = (year - 1) * 365 + day
    for m in range(1, month):
        count += days[m]
    return count


start = datetime(*map(int, input().split(' ')))
end = datetime(*map(int, input().split(' ')))

d1 = count_days(start.year, start.month, start.day)
d2 = count_days(end.year, end.month, end.day)

t1 = time(start.hour, start.minute, start.second)
t2 = time(end.hour, end.minute, end.second)

if t2 < t1:
    print(d2 - d1 - 1, (end - start).seconds)
else:
    print(d2 - d1, (end - start).seconds)
