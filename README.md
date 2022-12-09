# NSE-data-retrieval

Code helps you to retrieve stock data from the NSE archive
## There are three different files in the repo
## 1. entire month collector.py
  - To get data for a particular month in a year
  - Change the following function ```old_data(year,month)```
    - Eg: Jan of 2020: ```old_data(2020,01)```
## 2. data retrive.py
  - This program helps to retrieve data from a particular day in the current month
  - Run the program and enter the date that you want to download (add 0 before single digit number)

## 3.extractor.py
  - This helps to extract downloaded Zip files to CSV
  - Just change the ```dir_name``` to your respective path
  -run the program to see the magic will happen in the very next seconds
#### Note:  Data may not be adjusted to corporate action
