from scousepy import scouse
from astropy.io import fits
import os
import sys
import numpy as np
from matplotlib import pyplot as plt
from astropy import wcs
from astropy.table import Table
from astropy.table import Column
from astropy.io import ascii

datadirectory =  './HC3N_TP_7m_12m_feather/stage_4/'
datafilename =  datadirectory+'best_fit_solutions.v2.refit.dat'

# Load in data
dataarr    = np.loadtxt(datafilename, skiprows=1)
# Data is organised as follows: x, y, peak intensity, error on peak intensity,
# velocity, FWHM linewidth, rms noise
dataarr = np.array(dataarr[:,np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])]).T

dataarr = dataarr[:, np.squeeze(np.where(dataarr[0,:] != 0.0))]
dataarr = dataarr[:, np.squeeze(np.where(dataarr[3,:] > dataarr[4,:]))]
dataarr = dataarr[:, np.squeeze(np.where(dataarr[7,:] > dataarr[8,:]))]
dataarr = dataarr[:, np.squeeze(np.where((dataarr[5,:] > 30.0) & (dataarr[5,:]<100.0)))]

headings = ['ncomps', 'x', 'y', 'amplitude', 'err amplitude', 'shift', 'err shift', 'width', 'err width', 'rms', 'residual', 'chisq', 'dof', 'redchisq', 'aic']

table = Table(meta={'name': 'best-fitting model solutions'})

for j in range(len(headings)):
    table[headings[j]] = Column(dataarr[j,:])

print(table)
table.write(datadirectory+'/best_fit_solutions.v2.refit.trimbadfits.dat', format='ascii', \
            overwrite=True, delimiter='\t')
