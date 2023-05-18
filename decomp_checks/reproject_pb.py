"""
@author:      Dylan Pare
@date:        03/24/2023
@name:        reproject_pb.py
@description: Rescale the primary beam obtained from Ginsburg (on Globus) to 
match WCS with the SgrB2 pilot data.
"""

# Import needed packages
import numpy as np
from reproject import reproject_interp
from astropy.io import fits
from astropy import wcs
import glob
import os

# Reproject the PB distribution to match WCS construction of the Sgr B2 data
path     = os.getcwd()
parent   = os.path.dirname(path)
pb_name  = parent + '/SgrB2_PrimaryBeam.fits'
WCS_name = parent + '/HC3N_TP_7m_12m_feather/stage_4/stage_4_AIC.fits' # Any image from stage 4 to get WCS
pb_im    = fits.open(pb_name)
WCS_im   = fits.open(WCS_name)
WCS_head = WCS_im[0].header

pb_im_new, footprint = reproject_interp(pb_im,WCS_head)

# Write out the new primary beam image with the appropriate pixel / WCS scaling
fits.writeto('Sgr_PrimaryBeam_new.fits',data=pb_im_new,header=WCS_head)

