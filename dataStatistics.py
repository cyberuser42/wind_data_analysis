import numpy as np

# This script calculates and returns a chosen statistic.
# Options are mean, variance and cross-correlation
# If the user chooses cross-correlation zref, yref and dx must also be supplied
def dataStatistics(data, statistic, zref=0, yref=0, dx=0):

    # Calculating mean on the x-axis (axis=2) with. The result is thus a z*y grid with mean values of the x-axis. 
    if statistic == "mean":
        result = np.mean(data, axis=2)
        return result

    # Calculating the variance on x-axis 
    if statistic == "variance":
        result = np.var(data, axis=2) 
        return result

    # Calculating the cross-correlation 
    if statistic == "cross-correlation":
        
        # First step is finding the size of the x-axis 
        nx = np.size(data,axis=2)

        # n is how far along the x-axis we need to sum 
        n = nx-dx
        
        # 
        result = data[:,:, 0:n] * data[zref, yref, dx:nx]
        result = (1/n)*np.sum(result, axis=2)
        
        return result
    
    else:
        print("Invalid input")