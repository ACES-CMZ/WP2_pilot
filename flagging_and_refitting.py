from scousepy import scouse
import sys
import glob
import os
import shutil
from scousepy.io import output_ascii_indiv
from scousepy.scousespatial import ScouseSpatial

# paths to important stuff - you shouldn't need to touch this
datadir='./'
outputdir='./'
filename='HC3N_TP_7m_12m_feather' # note we remove the fits extension

s1file='s1.combine.scousepy' # You will need to update these accordingly!!
s2file='s2.combine.scousepy' # You will need to update these accordingly!!
tolver='v2'

s4filerefit='s4.refit.scousepy.'+tolver

# output flags and fits
flags='s4.flags.'+tolver+'.scousepy'
flagsrefit='s4.refit.flags.'+tolver+'.scousepy'
flagmap='flagmap.'+tolver+'.fits'
flagmaprefit='flagmap.'+tolver+'.refit.fits'

# Run first two stages - stage 1 should simply load up the scouse file
# stage 2 will open the fitter.
#
# Once completed upload the decomposed stage 2 data to github and globus
config_file=scouse.run_setup(filename, datadir, outputdir=outputdir, verbose=False)
s = scouse.stage_1(config=config_file, interactive=False, s1file=s1file, verbose=False )
s = scouse.stage_2(config=config_file, refit=False, s1file=s1file, s2file=s2file, verbose=False)
s = scouse.stage_3(config=config_file+str('.'+tolver), s1file=s1file, s2file=s2file, s3file='s3.scousepy.'+tolver, verbose=False)
s = scouse.stage_4(config=config_file+str('.'+tolver), s1file=s1file, s2file=s2file, s3file='s3.scousepy.'+tolver, s4file='s4.refit.scousepy.2.1', bitesize=True, nocheck=False, verbose=False)

#output_ascii_indiv(s, datadir+filename+'/stage_4/', filename='best_fit_solutions'+str('.'+tolver)+'refit.dat')

# fitsimages=[os.path.join(datadir+filename+'/stage_4/stage_4_AIC.fits'),
#             os.path.join(datadir+filename+'/stage_4/stage_4_chisq.fits'),
#             os.path.join(datadir+filename+'/stage_4/stage_4_ncomps.fits'),
#             os.path.join(datadir+filename+'/stage_4/stage_4_redchisq.fits'),
#             os.path.join(datadir+filename+'/stage_4/stage_4_residstd.fits'),
#             os.path.join(datadir+filename+'/stage_4/stage_4_rms.fits')]
#
# for file in fitsimages:
#     if os.path.exists(file):
#         splitfits=file.split('.fits')[0]
#         fitsimageupdated=splitfits+str('.'+tolver+'.refit.fits')
#         shutil.copyfile(file, fitsimageupdated)
#         os.remove(file)
#
# stats = scouse.compute_stats(s)
#
# print("total number of pixels: ", stats.nspec)
# print("number of spectral averaging areas: ", stats.nsaa)
# print("number of spectra contained within the SAAs: ", stats.nspecsaa)
# print("Number of those spectra actually fit: ", stats.nfits)
# print("Total number of Gaussians: ", stats.ncomps)
# print("Number of pixels with ncomps > 1: ", stats.nmultiple)
# print("Components per pixel: ", stats.ncompsperfit)
#
# spatial = ScouseSpatial(scouseobject=s, njobs=20, flag_sigma=1)
# spatial.flagging(s.indiv_dict)
# spatial.create_flag_map(s.indiv_dict, outputfits=flagmap)
# spatial.save_flags(outputfile=flags)
# # spatial = ScouseSpatial.load_flags(datadir+filename+'/stage_4/'+flags)
#
# statdict=spatial.stats()
# print(stats.nspec, stats.nspecsaa, statdict)
# #
# # tol0 = [3.0,3.0,1.0,2.5,2.5,0.5]
# # tol1 = [4.0,3.0,1.0,4.0,4.0,0.5]
# #tol2 = [4.0,3.0,0.5,5.0,5.0,0.5]
# tol3 = [4.0,3.0,1.0,5.0,5.0,0.5]
# #
# spatial.spatial_refit(s, refitfile=s4filerefit, tol=tol3)
# spatial.create_flag_map(s.indiv_dict, outputfits=flagmaprefit)
# spatial.save_flags(outputfile=flagsrefit)
# statdict=spatial.stats()
# print(stats.nspec, stats.nspecsaa, statdict)
