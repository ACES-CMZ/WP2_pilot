from scousepy import scouse

# paths to important stuff - you shouldn't need to touch this
datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

s1file='s1.combine.scousepy' # You will need to update these accordingly!!
s2file='s2.combine.scousepy' # You will need to update these accordingly!!
tolver='v2'
# Run first two stages - stage 1 should simply load up the scouse file
# stage 2 will open the fitter.
#
# Once completed upload the decomposed stage 2 data to github and globus
config_file=scouse.run_setup(filename, datadir, outputdir=outputdir)
s = scouse.stage_1(config=config_file, interactive=False, s1file=s1file )
s = scouse.stage_2(config=config_file, refit=False, s1file=s1file, s2file=s2file)
s = scouse.stage_3(config=config_file+str('.'+tolver), s1file=s1file, s2file=s2file, s3file='s3.scousepy.'+tolver)
s = scouse.stage_4(config=config_file+str('.'+tolver), s1file=s1file, s2file=s2file, s3file='s3.scousepy.'+tolver, s4file='s4.scousepy.'+tolver, bitesize=True)

from scousepy.io import output_ascii_indiv

output_ascii_indiv(s, datadir+filename+'/stage_4/', filename='best_fit_solutions'+str('.'+tolver)+'.dat')

stats = scouse.compute_stats(s)

print("total number of pixels: ", stats.nspec)
print("number of spectral averaging areas: ", stats.nsaa)
print("number of spectra contained within the SAAs: ", stats.nspecsaa)
print("Number of those spectra actually fit: ", stats.nfits)
print("Total number of Gaussians: ", stats.ncomps)
print("Number of pixels with ncomps > 1: ", stats.nmultiple)
print("Components per pixel: ", stats.ncompsperfit)
