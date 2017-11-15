#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fileRW import fileRW

"""The example to test fileRW class functions"""

# Initialize the testing data list
statistic = [[1,50],[2,100],[2,300]]

# The example of writting and reading for txt file.
file1 = fileRW("mnistdata.txt","./log_test/")
file1.writeTxt(statistic,",")
data = file1.readTxt( ",")
print "This is an example of reading/writting for txt file."
print data

# The example of writting and reading for xlsx file.
file2 = fileRW("mnistdata.xlsx")
file2.writeExcel("sheet1",statistic)  # Write data into sheet 
data = file2.readExcel(0)        # Read data from sheet 1
print "This is an example of reading/writting for excel file."
print data

file2.writeExcel("sheet2",statistic, ['H1','H2']) # With header
print "This is an example of reading/writting for excel file data with header."
data = file2.readExcel(0)         # Read data from sheet 2
print data
