"""
(sunday ... saturday) = (0 ... 6)

1 Jan 1900 was a Monday 
so start of month = 1
for every month, start of next month is ((no. of days in month)+start)%7
"""

def daysInMonth(yr):
    def isleap(yr):
        return yr%4==0 and (yr%100 != 0 or yr%400 == 0)
    if isleap(yr):
        feb = 29
    else:
        feb = 28
    return [31,feb,31,30,31,30,31,31,30,31,30,31]

def sunday(start,ndays):
    return (ndays+start)%7

Month = {0:"Jan",1:"Feb",2:"Mar",3:"Apr",4:"May",5:"Jun",
         6:"Jul",7:"Aug",8:"Sep",9:"Oct",10:"Nov",11:"Dec"}

start = 1 
months = []

for yr in xrange(1900,2001):
    days = daysInMonth(yr)
    for i in xrange(12):
        if start == 0 and yr>1900: 
            months.append( (Month[i],yr) )
        start = sunday(start,days[i])

print months        
print len(months)            
            
    
"""

import datetime
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print count

"""
