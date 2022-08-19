# To retrive a data for current month till today

# 
import calendar
import requests
from datetime import date, datetime

x = datetime.now()
month_list = []
ulr_list = []


def old_data(year, month_num=15):

    # given_month = month_number
    loop_month = month_num
    C_year = year
    


    # get current month as short version as well as month as number
    current_month = x.strftime("%b")
    month_number = x.strftime("%m")
    current_year = x.strftime("%Y")
    
    #checks whether it needs to go through full year or particular month
    
    if loop_month > 13:
        if int(C_year) == int(current_year):
            for y in range(1,int(month_number)+1):
                a_month = (calendar.month_abbr[y])  
                month_list.append(a_month)              
        else:   
            for i in range(1,13):
                b_month = (calendar.month_abbr[i])
                month_list.append(b_month)
    else:
        c_month = (calendar.month_abbr[int(month_num)])
        month_list.append(c_month)
        # pass
    Umonth_list = [x.upper() for x in month_list]
    
    # Creates a URL for evenry day
    for a in Umonth_list:
        for date in range(1,31):
            
            data = ("https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{Ydate}{month}{year}bhav.csv.zip".format(year= C_year, month=a,Ydate =date))
            ulr_list.append(data)

    print(ulr_list)
old_data(2021,1)
# download = requests.get(nse)a
# print(nse)
# pass
