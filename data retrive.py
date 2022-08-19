import calendar
from time import time
import zipfile
import requests
from zipfile import ZipFile
import os
from datetime import date, datetime
x= datetime.now()

def get_data(time_frame):
    date = time_frame
    C_year = x.strftime("%Y")
    # date = x.strftime("%d")
    C_month = x.strftime("%b").upper()
    data = ("https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{Ydate}{month}{year}bhav.csv.zip".format(year= C_year, month=C_month,Ydate =date))
    print(data)
    File_name = ("{date}_{month}_{year}.zip".format(date= date,month=C_month, year= C_year ))
    print(type(File_name))

    download = requests.get(data)
    with open (File_name,"wb") as f:
        f.write(download.content)
    with ZipFile(File_name,"r") as zip:
        zip.extractall()
    os.remove(File_name)    

input = int(input("Enter the required date within this month (add 0 if its single digit) "))

get_data(input)