# PyIO
The main goal of this project is to build the functions about daily computer works, make all jobs more efficiency. In addition, we hope the function of file read/write and data plot can help the people who need statistics analysis.
## Getting Started
Before use these class functions, we need to install some python plugins by instructions as follow, and the environment of mine is ubuntu 14.04LTS.
### Requirements
- Python 2.7
- xlrd
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
- `config/*`: Contains the configs of dataPlot class and doxygen.
- `docs/html/*`: Contains the objects of this PyIO project document.
- `images/*`: Contains the example graphs.
- `python`: Contains examples of file read/write and excel read/write.
- `dataPlot.py`: Class with graph plot functions.
- `example_dataPlot.py`: An example to show how to use dataPlot class.
- `example_fileRW.py`: An example to show how to use fileRW class.
- `fileRW.py`: Class with file read/write functions.

## Desciption
This part we give the examples to introduce how to use the fileRW class and dataPlot class, if we want to see more detail examples, we can see [example_fileRW.py](https://github.com/CrowGuy/PyIO/blob/master/example_fileRW.py) and [example_dataPlot.py](https://github.com/CrowGuy/PyIO/blob/master/example_dataPlot.py).
### Config of dataPlot class
The config of datPlot is [plotConfig.ini](https://github.com/CrowGuy/PyIO/blob/master/config/plotConfig.ini) which in config/ floder. This part we introduce the config details.
<img  width="420"  src="https://github.com/CrowGuy/PyIO/blob/master/images/Description_universal.png">
<img  width="420"  src="https://github.com/CrowGuy/PyIO/blob/master/images/Description_line.png">
<img  width="420"  src="https://github.com/CrowGuy/PyIO/blob/master/images/Description_scatter.png">
<img  width="420"  src="https://github.com/CrowGuy/PyIO/blob/master/images/Description_bar.png">
#### Universal config params
- `FigureXsize`: The image height, the value you set will multiply 100, unit is pixels.
- `FigureYsize`: The image width, the value you set will multiply 100, unit is pixels.
- `FigureDpi`: The Dots Per Inch of image.
- `GraphGrid`: Wether to set grid line in background, the value is *True* or *False*, default value is *True*.
- `GridStyle`: The style of grid, the default is *dotted*. 
- `ImgPath`: The path where images to save, the default path is *./images/*.
- `ImgName`: The image file name, default value are *Line_example.png*, *Scatter_example.png*, *Bar_example.png*.

#### Line plot config params
- `LineColor`: The color of line, more color value we can reference this [website](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html).
- `LineWidth`: The width of line.
- `LabelName`: The label name of every item.
- `MarkerType`: The marker type of line, more marker type we can reference this [website](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html).   

#### Scatter plot config params
- `ScatterColor`: The color of scatter, the color value we can reference this [website](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html).
- `GroupLabel`: The label name of every item.

#### Bar plot config params
- `BarColor`: The color of bar, more color value we can reference this [website](https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html).
- `BarWidth`: The width of bar.
- `GroupLabel`: The label name of every item.

### The PyIO project Documents
This project we use doxygen to generate the document, and the documt is [here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/CrowGuy/PyIO/master/docs/html/index.html). If you want to know the function and class in this project, we suggest you to read the document.
