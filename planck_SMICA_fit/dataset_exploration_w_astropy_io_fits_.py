 #testing 
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
from scipy import special

#import pyccl as ccl

from astropy.io import fits

# Open a FITS file
#hdul = fits.open('COM_CMB_IQU-smica_2048_R3.00_oe2.fits')
hdul = fits.open('HFI_Mask_GalPlane-apo2_2048_R2.00.fits')
print(hdul.info())
print(type(hdul))
print('--------------- :) --------------')

# Access primary HDU data
data = hdul[1].data
header = hdul[1].header

# Print metadata
print(header)
print('--------------- :) --------------')
print(data)


# Close file when done
hdul.close()