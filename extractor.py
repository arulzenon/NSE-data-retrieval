# To retrive a data for current month till today

# 

from platform import java_ver

from zipfile 
import os, zipfile

from datetime import  datetime

x = datetime.now()
month_list = []
ulr_list = []
output_dir = './NSE_data'
zip_file = ".zip"
dir_name = 'D:/python/Stock market data/NSE_data'
os.chdir(dir_name)

def extraction():
    print("extraction called for...")
    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(zip_file): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name)




