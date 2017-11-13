#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import ConfigParser

class dataPlot(object):
    """docstring for dataPlot"""
    def __init__(self, data, multi, title, save_bit):
        self.data = data            # The data of x and y
        self.title = title          # Title of graph
        self.save_bit = save_bit    # Whether save or not
        self.config = ConfigParser.ConfigParser()
        self.multi = multi

        self.y = []

        self.data = map(list, zip(*self.data))
        self.x = self.data[0]
        for ind in range(len(self.data)-1):
            self.y.append(self.data[ind+1])
        

    def linePlot(self, xname='', yname=''):
        """docstring for linePlot"""
        # Read the params from Config
        self.config.read('plotConfig.ini')
        self.graph = 'Line'
        line_color = self.config.get(self.graph, 'LineColor').split(',')
        line_width = self.config.get(self.graph, 'LineWidth').split(',')
        label_name = self.config.get(self.graph, 'LabelName').split(',')
        marker_type = self.config.get(self.graph, 'MarkerType').split(',')
        graph_grid = self.config.get(self.graph, 'GraphGrid')
        grid_style = self.config.get(self.graph, 'GridStyle')

        plt.grid(graph_grid,linestyle=grid_style)
        plt.title(self.title)
        plt.xlabel(xname)
        plt.ylabel(yname)
        if not self.multi:
            plt.plot(self.x, self.y, color=line_color[0], \
                                     linewidth=float(line_width[0]) , \
                                     label=label_name[0], \
                                     marker=marker_type[0])
            plt.legend(borderaxespad=0, bbox_to_anchor=(1.08,1))
            plt.subplots_adjust(right=0.8)
            plt.show()
        else:
            for ind, y in enumerate(self.y):
                plt.plot(self.x, y, color=line_color[ind], \
                                    linewidth=float(line_width[ind]), \
                                    label=label_name[ind], \
                                    marker=marker_type[ind])
            plt.legend(borderaxespad=0, bbox_to_anchor=(1.30,1))
            plt.subplots_adjust(right=0.8)
            plt.show()

    def scatterPlot(self, xname, yname):
        """docstring for scatterPlot"""
        # Read the params from Config
        self.config.read('plotConfig.ini')
        self.graph = 'Scatter'
        scat_color = self.config.get(self.graph, 'ScatterColor').split(',')
        scat_group = self.config.get(self.graph, 'GroupLabel').split(',')
        graph_grid = self.config.get(self.graph, 'GraphGrid')
        grid_style = self.config.get(self.graph, 'GridStyle')
        
        plt.grid(graph_grid, linestyle=grid_style)
        plt.title(self.title)
        plt.xlabel(xname)
        plt.ylabel(yname)

        if not self.multi:
            plt.scatter(self.x, self.y, c=scat_color[0], \
                                        label=scat_group[0])
            plt.legend(borderaxespad=0, bbox_to_anchor=(1.04,1))
            plt.subplots_adjust(right=0.9)
            plt.show()
        else:
            for ind, y in enumerate(self.y):
                plt.scatter(self.x, y, c=scat_color[ind], \
                                       label=scat_group[ind])
            plt.legend(borderaxespad=0, bbox_to_anchor=(1.04,1))
            plt.subplots_adjust(right=0.9)
            plt.show()

    def barPlot(self, xname='', yname=''):
        """docstring for barPlot"""        
        # Read the params from Config
        self.config.read('plotConfig.ini')
        self.graph = 'Bar'
        N = np.arange(len(self.x))
        bar_color = self.config.get(self.graph, 'BarColor').split(',')
        bar_width = self.config.get(self.graph, 'BarWidth').split(',')
        bar_group = self.config.get(self.graph, 'GroupLabel').split(',')
        graph_grid = self.config.get(self.graph, 'GraphGrid')
        grid_style = self.config.get(self.graph, 'GridStyle')

        plt.grid(graph_grid, linestyle=grid_style)
        plt.title(self.title)
        plt.xlabel(xname)
        plt.ylabel(yname)
        if not self.multi:
            plt.xticks(N, self.x)
            plt.bar(N, self.y, width=float(bar_width[0]), \
                               color=bar_color[0])
            plt.legend(bar_group[0], borderaxespad=0, \
                                     bbox_to_anchor=(1.04,1))
            plt.subplots_adjust(right=0.95)
            plt.show()
        else:
            plt.xticks(N + float(bar_width[0]), self.x)
            for ind, y in enumerate(self.y):    
                plt.bar(N + ind*float(bar_width[ind]), y, 
                        width=float(bar_width[ind]), 
                        color=bar_color[ind])
            plt.legend(bar_group, borderaxespad=0, bbox_to_anchor=(1.04,1))
            plt.subplots_adjust(right=0.95)
            plt.show()


    def boxPlot(self):
        """docstring for boxPlot"""
        
if __name__ == '__main__':
    item_single = [[100,95],[150,92],[200,90.1],\
                   [250,89.53],[300,87.78],[350,85.24],\
                   [400,79.89],[450,76.46],[500,72.88]]
    item_multi = [[100,95,97],[150,92,96],[200,90.1,93.4],\
                  [250,89.53,91.6],[300,87.78,89.92],[350,85.2,87.1],\
                  [400,79.89,84.29],[450,76.4,80.1],[500,72.8,76.5]]

    #graph1 = dataPlot(item_single, 'Example 01', False)
    #graph1.linePlot(False,'#','%')
    #graph1.scatterPlot(False, '#','%')
    #graph1.barPlot(False, '#', '%')
    graph2 = dataPlot(item_multi, True, 'Example 01', False)
    graph2.linePlot('#','%')
    graph2.scatterPlot('#','%')
    graph2.barPlot('#', '%')

