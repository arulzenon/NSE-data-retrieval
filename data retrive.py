### data retrive from stock market
import calendar
from datetime import datetime
from time import strftime
C_year = 2022
list2 = []
x = datetime.now()
month_number = x.strftime("%m")


list = []
for i in range(1,int(month_number)):

    val = (calendar.month_abbr[i])
    # print(datetime.strftime(i, %m))
    list.append(val)
    # print(val)

# list.pop(0)
print(list)

for a in list:
    for date in range(1,32):
        
        # list2.append(dates)
        data = ("https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{Ydate}{month}{year}bhav.csv.zip".format(year= C_year, month=a,Ydate =date ))
        list2.append(data)
print(list2)
# # print(month_number)
# print(type(month_number))

# y = range(int(month_number))
# print(y)
