#Solution 1
from datetime import datetime
date = "Oct 14 1997 7:15AM"
print(type(date))
date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)
print(type(date_time))

#solution 2 Using dateutil Module

from dateutil import parser

date_t = parser.parse("Oct 14 1997 7:15AM")

print(date_t)

print(type(date_t))


