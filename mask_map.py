p = "/Users/henshaw/Dropbox/Work/Code/GitHub/phangs_imaging_scripts/"
import sys
sys.path.append(p)
from phangsPipeline import scMaskingRoutines
from astropy.io import fits
import astropy.units as u
import numpy as np
from spectral_cube import SpectralCube

datadir='./'
cube=datadir+'HC3N_TP_7m_12m_feather.fits'
noise_cube='HC3N_TP_7m_12m_feather.noise.fits'

output_mask3d='HC3N_TP_7m_12m_feather.mask3d.fits'
output_mask2d='HC3N_TP_7m_12m_feather.mask2d.fits'

# spcube=SpectralCube.read(cube)
spcuben=SpectralCube.read(noise_cube)
spcubenmask = (spcuben > u.Quantity(0.1,spcuben.unit))
#
# spcube_mask=spcube.with_mask(spcubemask)
spcuben_mask=spcuben.with_mask(spcubenmask)

mask3d=scMaskingRoutines.recipe_phangs_strict_mask(cube,spcuben_mask,outfile=output_mask3d,overwrite=True,
                                                   mask_kwargs={"hi_thresh": 5, "lo_thresh": 2.5, "hi_nchan": 4, "lo_nchan":2})
mask3dhdu = fits.open(output_mask3d)
header=mask3dhdu[0].header
header.remove('CRPIX3')
header.remove('CRVAL3')
header.remove('CDELT3')
header.remove('CUNIT3')
header.remove('CTYPE3')
mask2d = np.nanmax(mask3d, axis=0)
hdu = fits.PrimaryHDU(data=mask2d, header=header)
hdu.writeto(output_mask2d, overwrite=True)
