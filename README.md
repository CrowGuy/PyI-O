# PyI-OI
The main goal of this project is to build the functions about daily computer works, make all jobs more efficiency. In addition, we hope the function of file read/write and data plot can help the people who need statistics analysis.
## Getting Started
Before use these class functions, we need to install some python plugins by instructions as follow, and the environment of mine is ubuntu 14.04LTS, pyhton 2.7.
```
$ sudo apt-get install python-pip
```
### Installing
Install the plugins for reading and writting excel file.
```
$ sudo pip install xlrd xlwt
```
Because xlwt is only support excel 2003, so we need to install xlsxwritter.
```
$ sudo pip install xlsxwriter
```
Install matplotlib for plotting statistics graph.
```
$ sudo pip install matplotlib
$ sudo apt-get install python-tk
```
## Running the examples
This part we give the examples to introduce how to use the fileRW class and dataPlot class, if we want to see more detail examples, we can see [example_fileRW.py](https://github.com/CrowGuy/PyIO/blob/master/example_fileRW.py) and [example_dataPlot.py](https://github.com/CrowGuy/PyIO/blob/master/example_dataPlot.py).
### fileRW
```
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
```
### dataPlot
```
item_single = [[100,95],[150,92],[200,90.1],\
               [250,89.53],[300,87.78],[350,85.24],\
               [400,79.89],[450,76.46],[500,72.88]]
item_multi = [[100,95,97],[150,92,96],[200,90.1,93.4],\
              [250,89.53,91.6],[300,87.78,89.92],[350,85.2,87.1],\
              [400,79.89,84.29],[450,76.4,80.1],[500,72.8,76.5]]

# The example of single y axis value data
graph1 = dataPlot(item_single, False, 'Example 01', False)
graph1.linePlot('#','%')
graph1.scatterPlot('#','%')
graph1.barPlot('#', '%')

# The example of multi y axis value data
graph2 = dataPlot(item_multi, True, 'Example 02', False)
graph2.linePlot('#','%')
graph2.scatterPlot('#','%')
graph2.barPlot('#', '%')
```
