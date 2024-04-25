p = "/Users/henshaw/Dropbox/Work/Code/GitHub/phangs_imaging_scripts/"
import sys
sys.path.append(p)
from phangsPipeline import scNoiseRoutines
from astropy.io import fits
import numpy as np

datadir='./'
cube=datadir+'HC3N_TP_7m_12m_feather.fits'

output_noise='HC3N_TP_7m_12m_feather.noise.new.fits'

# run noise routine
noise=scNoiseRoutines.recipe_phangs_noise(cube,outfile=output_noise,overwrite=True,)
