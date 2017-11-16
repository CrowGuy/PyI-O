# PyI-OI
The main goal of this project is to build the functions about daily computer works, make all jobs more efficiency. In addition, we hope the function of file read/write and data plot can help the people who need statistics analysis.
## Getting Started
Before use these class functions, we need to install some python plugins by instructions as follow, and the environment of mine is ubuntu 14.04LTS, pyhton 2.7.
### Requirements
- Python 2.7
- xlsxwriter
- matplotlib

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
## Content
- `config/*`: The configs of dataPlot class.
- `python`: Contains examples of file read/write and excel read/write.
- `dataPlot.py`: Class with graph plot functions.
- `example_dataPlot.py`: An example to show how to use dataPlot class.
- `example_fileRW.py`: An example to show how to use fileRW class.
- `fileRW.py`: Class with file read/write functions.

## Usage
This part we give the examples to introduce how to use the fileRW class and dataPlot class, if we want to see more detail examples, we can see [example_fileRW.py](https://github.com/CrowGuy/PyIO/blob/master/example_fileRW.py) and [example_dataPlot.py](https://github.com/CrowGuy/PyIO/blob/master/example_dataPlot.py).


