import time
import pytz
print(time.time())

import datetime

d = datetime.datetime.now()

print(d, type(d))

print(dir(d))

print(d.weekday())
print(d.year, d.month, d.day)

d2 = datetime.datetime(year=2022, month=2, day=11)

date_str = '2023-02-28 14:30:00'
date_format = '%Y-%m-%d %H:%M:%S'

date_obj = datetime.datetime.strptime(date_str, date_format)
print(date_obj)


td = d - d2

print(td, type(td))
print(date_obj + td)

print(d)

d3 = datetime.datetime.utcnow().astimezone(tz=pytz.UTC)

print(d, d3)

print(d > d3)