# To retrive a data for current month till today

# 
import calendar
from platform import java_ver
import requests
from zipfile import ZipFile
import os
import wget
from datetime import date, datetime

x = datetime.now()
month_list = []
ulr_list = []
# output_dir = "D:\NSE Stock data"
file_name = "NSE data"
zipf = ".zip"


def old_data(year, month_num=15):    
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

    # print(Umonth_list)
    
    # Creates a URL for every day
    for a in Umonth_list:
        for date in range(1,31):
            DDdate = str(date)
            data = ("https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{Ydate}{month}{year}bhav.csv.zip".format(year= C_year, month=a,Ydate =DDdate.zfill(2)))
            ulr_list.append(data)
    print("stage worked")
    # print(ulr_list[-2])
    
    # Starts to download file for every day
    for links in ulr_list:
        print(links)
        wget.download(links)
        
        # for i in range(len(ulr_list)):
        #     download = requests.get(links)
        #     status_code = download.status_code
        #     print(status_code)
        #     # if  status_code > 0:
        # with open (file_name,"wb") as f:
        #     f.write(download.content)


            
        

# wget.download("https://archives.nseindia.com/content/historical/EQUITIES/2022/AUG/cm19AUG2022bhav.csv.zip") 
old_data(2021,1)
# download = requests.get(nse)a
# print(nse)
# pass
