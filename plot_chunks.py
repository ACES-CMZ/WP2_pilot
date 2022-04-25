from astropy.io import fits
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from astropy.wcs import WCS
import glob
from scousepy import scouse
from matplotlib.pyplot import cm

try:
    from astropy.visualization.wcsaxes import WCSAxes
    _wcaxes_imported = True
except ImportError:
    _wcaxes_imported = False
    if coverageobject.moments[0].wcs is not None:
        warnings.warn("`WCSAxes` required for wcs coordinate display.")

fig = plt.figure(figsize=(14, 8))
blank_window_ax=[0.1,0.1,0.8,0.8]
newaxis=[blank_window_ax[0]+0.03, blank_window_ax[1]+0.03, blank_window_ax[2]-0.06,blank_window_ax[3]-0.045]

mom0 = fits.open('HC3N_TP_7m_12m_feather/stage_1/HC3N_TP_7m_12m_feather_mom0.fits')[0]

mom0header=mom0.header
mom0data=mom0.data

ax_image = WCSAxes(fig, newaxis, wcs=WCS(mom0header), slices=('x','y'))
map_window = fig.add_axes(ax_image)
x = map_window.coords[0]
y = map_window.coords[1]
x.set_ticklabel(exclude_overlapping=True)
y.set_ticklabel(rotation=90,verticalalignment='bottom', horizontalalignment='left',exclude_overlapping=True)

vmin=np.nanmin(mom0data)-0.05*np.nanmin(mom0data)
vmax=np.nanmax(mom0data)-0.55*np.nanmax(mom0data)

im=map_window.imshow(mom0data, cmap=plt.cm.binary_r, origin='lower',
                     interpolation='nearest', vmin=vmin,vmax=vmax)

s1files=np.asarray(glob.glob('HC3N_TP_7m_12m_feather/stage_1/*.scousepy'))

datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

s1filesvall=[file.split('stage_1/s1.')[1] for file in s1files]
s1filesval=[int(file.split('.scousepy')[0]) for file in s1filesvall]

sort_index = np.argsort(s1filesval)
s1files=s1files[sort_index]

n = len(s1files)
colour=iter(cm.rainbow(np.linspace(0,1,n)))

for file in s1files:
    c=next(colour)
    config_file=scouse.run_setup(filename, datadir, outputdir=outputdir)
    s1file=file.split('stage_1/')[1]
    s = scouse.stage_1(config=config_file, interactive=False, s1file=s1file)
    saa_dict=s.saa_dict[0]
    for index, saa in saa_dict.items():
        keys=[key for key in saa_dict.keys()]
        lastkey=keys[-1]
        if saa.to_be_fit:
            coords=saa.coordinates
            xy = (coords[0]-12.5, coords[1]-12.5)
            if index==lastkey:
                saapatch = patches.Rectangle(xy, 25, 25, alpha=0.4, facecolor=c, edgecolor='black', label=s1file)
                map_window.add_patch(saapatch)
            else:
                saapatch = patches.Rectangle(xy, 25, 25, alpha=0.4, facecolor=c, edgecolor='black')
                map_window.add_patch(saapatch)

map_window.legend(bbox_to_anchor=(1.01, 1.0))

plt.savefig('chunks.pdf', dpi=300,bbox_inches='tight')
