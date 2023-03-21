"""
@author: Dylan Pare
@date: 03/14/2023
@name: apply_mask.py
@description: apply the masks to the decomposition data files, removing the entries for the pixels that are marked by the mask file.
"""

# Import needed packages
import numpy as np
from astropy.io import ascii
from astropy.table import Table
from astropy.io import fits
import glob
import os

# Get paths to needed files and file basenames
path = os.getcwd()
parent = os.path.dirname(path)
dat_dir    = parent + '/HC3N_TP_7m_12m_feather/stage_4/'
dat_files  = glob.glob(dat_dir + '*refit.dat')
mask_files = glob.glob(dat_dir + '*mask.fits')
dat_names  = [os.path.basename(x) for x in glob.glob(dat_dir+'*refit.dat')]

# Read in the mask and the corresponding data file and remove the data entries that have been marked by the mask
for file in range(len(dat_files)):
	tab_dat = Table.read(dat_files[file],format='ascii')
	ncomps = tab_dat['ncomps']
	x = tab_dat['x']
	y = tab_dat['y']
	amp = tab_dat['amplitude']
	err_amp = tab_dat['err amplitude']
	shift = tab_dat['shift']
	err_shift = tab_dat['err shift']
	width = tab_dat['width']
	err_width = tab_dat['err width']
	rms = tab_dat['rms']
	residual = tab_dat['residual']
	chisq = tab_dat['chisq']
	dof = tab_dat['dof']
	redchisq = tab_dat['redchisq']
	aic = tab_dat['aic']

	mask_name = mask_files[file]
	prefix = dat_names[file][:-4]
	mask_im   = fits.open(mask_name)
	mask_dat  = mask_im[0].data
	mask_head = mask_im[0].header

	ncomps_thresh    = []
	x_thresh         = []
	y_thresh         = []
	amp_thresh       = []
	err_amp_thresh   = []
	shift_thresh     = []
	err_shift_thresh = []
	width_thresh     = []
	err_width_thresh = []
	rms_thresh       = []
	residual_thresh  = []
	chisq_thresh     = []
	dof_thresh       = []
	redchisq_thresh  = []
	aic_thresh       = []
	for xi in range(len(x)):
		if mask_dat[int(y[xi])][int(x[xi])] == 0:
			ncomps_thresh.append(ncomps[xi])
			x_thresh.append(x[xi])
			y_thresh.append(y[xi])
			amp_thresh.append(amp[xi])
			err_amp_thresh.append(err_amp[xi])
			shift_thresh.append(shift[xi])
			err_shift_thresh.append(err_shift[xi])
			width_thresh.append(width[xi])
			err_width_thresh.append(err_width[xi])
			rms_thresh.append(rms[xi])
			residual_thresh.append(residual[xi])
			chisq_thresh.append(chisq[xi])
			dof_thresh.append(dof[xi])
			redchisq_thresh.append(redchisq[xi])
			aic_thresh.append(aic[xi])

	print(len(x))
	print(len(x_thresh))

	tab_dat_new = Table([ncomps_thresh,x_thresh,y_thresh,amp_thresh,err_amp_thresh,shift_thresh,err_shift_thresh,width_thresh,err_width_thresh,rms_thresh,residual_thresh,chisq_thresh,dof_thresh,redchisq_thresh,aic_thresh],names=('ncomps','x','y','amplitude','err amplitude','shift','err shift','width','err width','rms','residual','chisq','dof','redchisq','aic'))
	tab_dat_new.write(prefix+'_mask.dat',format='ascii')
