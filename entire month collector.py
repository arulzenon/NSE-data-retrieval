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
output_dir = './NSE_data'




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
        for date in range(1,32):
            DDdate = str(date)
            data = ("https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{Ydate}{month}{year}bhav.csv.zip".format(year= C_year, month=a,Ydate =DDdate.zfill(2)))
            ulr_list.append(data)
    print("stage worked")
    # print(ulr_list[-2])
    
    # Starts to download file for every day
    for links in range(len(ulr_list)):
        
        
        running_site = ulr_list[links]
        print(running_site)
        web_status = requests.get(running_site,allow_redirects=False).is_redirect
        print(web_status)
        
        if web_status == False:
        
            wget.download(running_site, out=output_dir)

    
        
        

            
        

# wget.download("https://archives.nseindia.com/content/historical/EQUITIES/2022/AUG/cm19AUG2022bhav.csv.zip") 
old_data(2021,1)
# download = requests.get(nse)a
# print(nse)
# pass