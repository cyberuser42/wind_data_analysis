from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
from dataStatistics import *
import numpy as np

def dataPlot(data, stat, zref=0, yref=0, dx=0):
    ax = plt.subplot()
    data_plot = dataStatistics(data, statistic=stat, zref=zref, yref=yref, dx=dx)
    z = np.arange(np.size(data_plot[1,:]))
    y = np.arange(np.size(data_plot[:,1]))
    z,y = np.meshgrid(z,y)
    im = plt.contour(z,y,data_plot)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    mappable = plt.cm.ScalarMappable()
    plt.colorbar(mappable,cax)