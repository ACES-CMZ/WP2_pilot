from scousepy import scouse

# paths to important stuff
datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

config_file=scouse.run_setup(filename, datadir, outputdir=outputdir)
scouse.combine_chunks(config=config_file, nchunks=30 )
