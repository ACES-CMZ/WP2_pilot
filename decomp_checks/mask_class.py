"""
@author:      Dylan Pare
@date:        03/30/2023
@name:        mask_class.py
@description: Make a generate class allowing for the construction of different masks based on 
different parameters. Also have a routine to combine all generated masks to produce a final mask
for distribution.
"""
# Import needed packages
class MaskClass:
	"""Class for making and combining various masks."""

	def __init__(self):
		"""Initialization function for MaskClass.
		Inputs:
		None
		Outputs:
		None
		"""
		print("Please specify which masks to use [Mark True to use, else leave blank]: ")
		#prompt_thresh = input("Do you want to update thresholds? [defaults: ncomps = 8, AIC = -360.0, PB = 0.5, rms = 3.0, chisq = 10.0, redchisq = 1.0, residstd = 1.0]: ")

		params = {'ncomps': False,\
			'AIC': False,\
			'PB': False,\
			'rms' : False,\
			'chisq' : False,\
			'redchisq' : False,\
			'residstd' : False}

		thresh = {'ncomps' : 8,\
			'AIC' : -360.0,\
			'PB' : 0.5,\
			'rms' : 3.0,\
			'chisq' : 10.0,\
			'redchisq' : 1.0,\
			'residstd' : 1.0}

		ncomps = input("ncomps: ")
		AIC = input("AIC: ")
		PB = input("PB: ")
		rms = input("rms: ")
		chisq = input('chisq: ')
		redchisq = input('redchisq: ')
		residstd = input('residstd: ')	
		
		if ncomps == "True":
			params.update({"ncomps" : True})
		if AIC == "True":
			params.update({"AIC" : True})
		if PB == "True":
			params.update({"PB" : True})
		if rms == "True":
			params.update({"rms" : True})
		if chisq == "True":
			params.update({"chisq" : True})
		if redchisq == "True":
			params.update({"redchisq" : True})
		if residstd == "True":
			params.update({"residstd" : True})

		print("Default threshold levels for the different parameters: ncomps = 8, AIC = -360.0, PB = 0.5, rms = 3.0, chisq = 10.0, residstd = 1.0 [all except for AIC and PB are placeholders]")
		
		data_dir = 'data_dir'
		mask_dir = 'mask_dir'
		decomps  = ['v0','v1','v2']

		self.params = params
		self.thresh = thresh
		self.data_dir = data_dir
		self.mask_dir = mask_dir
		self.decomps = decomps
		return

	def make_mask(self):
		"""Make a mask for each parameter flagged as True.
		Inputs:
		None
		Outputs:
		mask_list = aarray of the names for the individual masks generated
		"""
		mask_list = []
		value_list = list(self.params.values())
		key_list   = list(self.params.keys())
		for el in range(len(value_list)):
			if value_list[el] == True:
				print("Making mask based on " + key_list[el] + " threshold.")
				cutoff = value_list[el]
				mask_prefix = key_list[el] + "_mask"
				print(mask_prefix)

		return mask_list

	def super_mask(self,mask_list):
		"""Create a super mask incorporating all of the sub-masks generated by the make_mask routine.
		Inputs:
		mask_list = array of string names referencing the sub-masks from make_mask.
		"""
		return
