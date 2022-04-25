from scousepy import scouse

# paths to important stuff
datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

# Running this first - and manually modifying the config file for coverage
# adding:
#
# mask_coverage = 'HC3N_TP_7m_12m_feather.mask2d.fits'
# vel_range = [-75, 200.0]
# wsaa = [25]
#

config_file=scouse.run_setup(filename, datadir, outputdir=outputdir)
s = scouse.stage_1(config=config_file, interactive=False, nchunks=30 )
