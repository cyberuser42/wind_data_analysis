from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
from dataStatistics import *
import numpy as np


## This function plots the data with the chosen statistic. 
## Inputs are the data, chosen statistic and if the cross-correlation statistic is chosen the zref, yref and dx are also required as inputs
def dataPlot(data, stat, zref=0, yref=0, dx=0):

    # data_plot is the 2d array that the chosen statistic produces 
    data_plot = dataStatistics(data, statistic=stat, zref=zref, yref=yref, dx=dx)

    # Getting the size of the array to create the length and width of the plot
    z, y = np.arange(np.size(data_plot[1,:])), np.arange(np.size(data_plot[:,1]))

    # Shaping the data into a grid with dimensions z*y
    z,y = np.meshgrid(z,y)
    
    # Creating a contourf plot to show the values as colors with increasing intensity
    plot = plt.contourf(z,y,data_plot)
    
    # Plotting a colorbar to show what value the colors correspond to
    plt.colorbar(plot)

    # Showing the plot
    plt.show()