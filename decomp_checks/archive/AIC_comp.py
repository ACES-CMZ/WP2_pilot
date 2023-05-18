"""
@author:      Dylan Pare
@date:        03/27/2023
@name:        AIC_comp.py
@description: This code compares the AIC values obtained from the different scousepy decompositions to determine
the most likely of the three. It also determines the likelihood of the other models to minimize information loss.
"""

# Import needed packages
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from aplpy import FITSFigure
import os
import glob

# Now read in the AIC files from the decomposistions after masking
cwd       = os.getcwd()
parent    = os.path.dirname(cwd)
dat_dir   = parent + '/HC3N_TP_7m_12m_feather/stage_4/'
aic_files = glob.glob(dat_dir + '*AIC*_mask.fits')
aic_names = [os.path.basename(x) for x in glob.glob(dat_dir + '*AIC*_mask.fits')]
decomp_v  = ['v0','v1','v2']

# Now iterate over the non-masked lines of sight and determine which AIC value is the minimum
test_im  = fits.open(aic_files[0])
test_dat = test_im[0].data
header   = test_im[0].header

v0_v1_diff = np.empty(test_dat.shape)
v0_v2_diff = np.empty(test_dat.shape)
v1_v2_diff = np.empty(test_dat.shape)

v0_v1_diff[:] = np.nan
v1_v2_diff[:] = np.nan
v0_v2_diff[:] = np.nan

v0_head = fits.open(aic_files[0])[0].header
v1_head = fits.open(aic_files[1])[0].header
v2_head = fits.open(aic_files[2])[0].header

name_v0_v1 = 'v0_v1_AIC_diff.fits'
name_v0_v2 = 'v0_v2_AIC_diff.fits'
name_v1_v2 = 'v1_v2_AIC_diff.fits'

im_v0  = fits.open(aic_files[0])
im_v1  = fits.open(aic_files[1])
im_v2  = fits.open(aic_files[2])
dat_v0 = im_v0[0].data
dat_v1 = im_v1[0].data
dat_v2 = im_v2[0].data
for x in range(len(test_dat)):
	for y in range(len(test_dat[0])):
		if (np.isnan(dat_v0[x][y]) != True) and (np.isnan(dat_v1[x][y]) != True) and (np.isnan(dat_v2[x][y]) != True):
			v0_v1_diff[x][y] = dat_v0[x][y] - dat_v1[x][y]
			v0_v2_diff[x][y] = dat_v0[x][y] - dat_v2[x][y]
			v1_v2_diff[x][y] = dat_v1[x][y] - dat_v2[x][y]

# Save the minimum AIC maps for future use
fits.writeto(name_v0_v1,data=v0_v1_diff,header=v0_head,overwrite=True)
fits.writeto(name_v0_v2,data=v0_v2_diff,header=v1_head,overwrite=True)
fits.writeto(name_v1_v2,data=v1_v2_diff,header=v2_head,overwrite=True)


