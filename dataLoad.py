import numpy as np
# Tror vindhastighederne er i m/s og 
def dataLoad(filename, Nx, Ny, Nz):
    with open(filename, 'rb') as binary_file:
        data = np.fromfile(binary_file,np.single)
    if np.size(data) == Nx * Ny * Nz:
        data = np.reshape(data,(Nx,Ny,Nz)).T #nu er rækkefølgen omvendt nz, ny, nx
    else:
        print("Invalid data or dimensions")
    return data