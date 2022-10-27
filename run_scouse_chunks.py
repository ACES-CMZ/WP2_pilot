from scousepy import scouse

# paths to important stuff - you shouldn't need to touch this
datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

s1file='s1.7.scousepy' # You will need to update these accordingly!!
s2file='s2.7.scousepy' # You will need to update these accordingly!!

# Run first two stages - stage 1 should simply load up the scouse file
# stage 2 will open the fitter.
#
# Once completed upload the decomposed stage 2 data to github and globus
config_file=scouse.run_setup(filename, datadir, outputdir=outputdir)
s = scouse.stage_1(config=config_file, interactive=False, s1file=s1file )
s = scouse.stage_2(config=config_file, refit=True, s1file=s1file, s2file=s2file)
