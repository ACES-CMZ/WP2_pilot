"""
@author:      Dylan Pare
@date:        03/14/2023
@name:        plot_maskdist.py
@description: Plot the distributions obtained from the masked scouse data set.
"""

# Import needed packages
import numpy as np
from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
import glob
import os

# Get paths to needed files and file basenames
path = os.getcwd()
parent = os.path.dirname(path)
dat_dir    = parent + '/HC3N_TP_7m_12m_feather/stage_4/'
dat_files  = glob.glob(dat_dir + '*_mask.dat')
mask_files = [dat_dir + 'v0_mask.fits',dat_dir+'v1_mask.fits',dat_dir+'v2_mask.fits']
dat_names  = [os.path.basename(x) for x in glob.glob(dat_dir+'*_mask.dat')]
aic_files = glob.glob(dat_dir + '*AIC*.refit.fits')
chisq_files = glob.glob(dat_dir + '*chisq*.refit.fits')
redchisq_files = glob.glob(dat_dir + '*redchisq*.refit.fits')
ncomps_files = glob.glob(dat_dir + '*ncomps*.refit.fits')
rms_files = glob.glob(dat_dir + '*rms*.refit.fits')

# Read in the data file and plot new distributions based on the masked data
for file in range(len(dat_files)):
	mask_name = mask_files[file]
	mask_im   = fits.open(mask_name)
	mask_data = mask_im[0].data

	aic_name   = aic_files[file]
	chisq_name = chisq_files[file]
	redchisq_name = redchisq_files[file]
	ncomps_name = ncomps_files[file]
	rms_name = rms_files[file]
	AIC_head = fits.open(aic_name)[0].header
	chisq_head = fits.open(chisq_name)[0].header
	redchisq_head = fits.open(redchisq_name)[0].header
	ncomps_head = fits.open(ncomps_name)[0].header
	rms_head = fits.open(rms_name)[0].header

	aic_prefix      = aic_name[:-5]
	chisq_prefix    = chisq_name[:-5]
	redchisq_prefix = redchisq_name[:-5]
	ncomps_prefix   = ncomps_name[:-5]
	rms_prefix      = rms_name[:-5]

	AIC = np.empty(mask_data.shape)
	AIC[:] = np.nan
	chisq = np.empty(mask_data.shape)
	chisq[:] = np.nan
	ncomps = np.empty(mask_data.shape)
	ncomps[:] = np.nan
	redchisq = np.empty(mask_data.shape)
	redchisq[:] = np.nan
	rms = np.empty(mask_data.shape)
	rms[:] = np.nan

	tab_dat = Table.read(dat_files[file],format='ascii')
	ncomps_ind = tab_dat['ncomps']
	x = tab_dat['x']
	y = tab_dat['y']
	amp_ind = tab_dat['amplitude']
	err_amp_ind = tab_dat['err amplitude']
	shift_ind = tab_dat['shift']
	err_shift_ind = tab_dat['err shift']
	width_ind = tab_dat['width']
	err_width_ind = tab_dat['err width']
	rms_ind = tab_dat['rms']
	residual_ind = tab_dat['residual']
	chisq_ind = tab_dat['chisq']
	dof_ind = tab_dat['dof']
	redchisq_ind = tab_dat['redchisq']
	aic_ind = tab_dat['aic']

	for xi in range(len(x)):
		AIC[int(y[xi])][int(x[xi])] = aic_ind[xi]
		chisq[int(y[xi])][int(x[xi])] = chisq_ind[xi]
		ncomps[int(y[xi])][int(x[xi])] = ncomps_ind[xi]
		redchisq[int(y[xi])][int(x[xi])] = redchisq_ind[xi]
		rms[int(y[xi])][int(x[xi])] = rms_ind[xi]

	# Now save the new distributions using the masked data
	fits.writeto(aic_prefix+'_mask.fits',AIC,AIC_head,overwrite=True)
	fits.writeto(chisq_prefix+'_mask.fits',chisq,chisq_head,overwrite=True)
	fits.writeto(ncomps_prefix+'_mask.fits',ncomps,ncomps_head,overwrite=True)
	fits.writeto(redchisq_prefix+'_mask.fits',redchisq,redchisq_head,overwrite=True)
	fits.writeto(rms_prefix+'_mask.fits',rms,rms_head,overwrite=True)
