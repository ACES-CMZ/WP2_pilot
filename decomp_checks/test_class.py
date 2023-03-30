"""
@author:      Dylan Pare
@date:        03/30/2023
@name:        test_class.py
@description: Test the make_mask class.
"""

# Import needed packages
import mask_class

test = mask_class.MaskClass()
print(test.params)

mask_names = test.make_mask()
