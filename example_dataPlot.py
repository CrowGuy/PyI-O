#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataPlot import dataPlot

"""The function test example for dataPlot class"""
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
