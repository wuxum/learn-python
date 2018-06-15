#!/usr/bin/python
# website: https://pythonbasics.org/time-and-date/

import time

timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))
