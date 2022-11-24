import numpy as np

# This function loads the data
# Inputs are the filename and dimensions (nx, ny, nz). In the test data these are in the filename
def dataLoad(filename, nx, ny, nz):
    
    # Reading the file as a binary file and storing in the variable binary_file
    with open(filename, 'rb') as binary_file:
    
        # using numpy to read the variable with values interpreted as single precision FP. 
        data = np.fromfile(binary_file,np.single)
    
    
    # If the size of the data matches the dimensions we reshape and transpose the data.
    if np.size(data) == nx * ny * nz:

        # Reshaping to fit the given dimensions
        data = np.reshape(data,(nx,ny,nz))

        # Data input is in (x,y,z) and after transposing is in (z,y,x). 
        data = data.T 
        
        return data

    # If the data doesn't fit the given dimensions 
    else:
        print("Invalid data or dimensions")