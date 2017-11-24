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
- `config/*`: Contains the configs of dataPlot class.
- `python`: Contains examples of file read/write and excel read/write.
- `dataPlot.py`: Class with graph plot functions.
- `example_dataPlot.py`: An example to show how to use dataPlot class.
- `example_fileRW.py`: An example to show how to use fileRW class.
- `fileRW.py`: Class with file read/write functions.

## Usage
This part we give the examples to introduce how to use the fileRW class and dataPlot class, if we want to see more detail examples, we can see [example_fileRW.py](https://github.com/CrowGuy/PyIO/blob/master/example_fileRW.py) and [example_dataPlot.py](https://github.com/CrowGuy/PyIO/blob/master/example_dataPlot.py).
### dataPlot
The config of datPlot is [plotConfig.ini](https://github.com/CrowGuy/PyIO/blob/master/config/plotConfig.ini) which in config/ floder. This part we introduce the config details.
#### Universal config params
![Universal config params](https://github.com/CrowGuy/PyIO/blob/master/images/Description_universal.png){:height="36px" width="36px"}.
- `FigureXsize`: The image height, the value you set will multiply 100, unit is pixels.
- `FigureYsize`: The image width, the value you set will multiply 100, unit is pixels.
- `FigureDpi`:
- `GraphGrid`: Wether to set grid line in background, the value is *True* or *False*, default value is *True*.
- `GridStyle`: The style of grid, the default is *dotted*. 
- `ImgPath`: The path where images to save, the default path is *./images/*.
- `ImgName`: The image file name, default value are *Line_example.png*, *Scatter_example.png*, *Bar_example.png*.

#### Line plot config params
<img align="center" width="450"  src="https://github.com/CrowGuy/PyIO/blob/master/images/Description_line.png">

- `LineColor`: The color of line, more color value we can reference this [website].
- `LineWidth`: The width of line.
- `LabelName`: The label name of every item.
- `MarkerType`: The marker type of line, more marker type we can reference this [website].   

#### Scatter plot config params
![Scatter config params](https://github.com/CrowGuy/PyIO/blob/master/images/Description_scatter.png){:height="36px" width="36px"}.
- `ScatterColor`: The color of scatter, the color value we can reference this [website].
- `GroupLabel`: The label name of every item.

#### Bar plot config params
![Bar config params](https://github.com/CrowGuy/PyIO/blob/master/images/Description_bar.png){:height="36px" width="36px"}.
- `BarColor`: The color of bar, more color value we can reference this [website].
- `BarWidth`: The width of bar.
- `GroupLabel`: The label name of every item.
