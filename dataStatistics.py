import numpy as np
def dataStatistics(data, statistic, zref=0, yref=0, dx=0):
    result = 0
    if statistic == "mean":
        result = np.mean(data, axis=2)
    if statistic == "variance":
        result = np.var(data, axis=2) 
    if statistic == "cross-correlation":
        nx = np.size(data,axis=2)
        n = nx-dx
        stat_data = data[:,:, 0:n] * data[zref, yref, dx:nx]
        result = (1/n)*np.sum(stat_data, axis=2)
    return result