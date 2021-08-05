import os
import numpy as np
from scipy import ndimage, interpolate
from scipy.ndimage import zoom
from processing import load_data, rescale_img, plot_scans

from KevinSR import SOUP_GAN

DIR_dicom = "./Sag_T1_MPRAGE_thick" 
pre_slices = 32
post_slices = 160


thicks_ori = load_data(DIR_dicom)
Z_FAC = post_slices/pre_slices # Sampling factor in Z direction

thicks_ori = rescale_img(thicks_ori, max_val= 10000)

thins = zoom(thicks_ori, (1,1,Z_FAC))
thins_raw = zoom(thicks_ori, (1,1,Z_FAC),order=0)

# Call the SR interpolation tool from KevinSR
thins_gen = SOUP_GAN(thicks_ori, 5)

# Plot the original thick slices, thin slices by TCI and SR generated slices. 
plot_scans(thins_raw, thins, thins_gen)


