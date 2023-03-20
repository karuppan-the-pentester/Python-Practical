import math
decibel = 10 * math.log10(18.0)
angle = 2.5
height = math.sin(angle)
print(decibel)
print(height)

import math
degree = 45
angle = degree * 2 * math.pi/360.0
print(math.cos(angle))

import time;
localtime = time.localtime(time.time())
print("Local current time :",localtime)
localtimestandard = time.asctime(time.localtime(time.time()))
print(localtimestandard)

import calendar
c=calendar.month(2022,5)
print(c)


import math
list=dir(math)
print(list)
help(math.sin)
