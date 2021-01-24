# 2. How to create a series from a list, numpy array and dict?

# Input

import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# My Solution

import pandas as pd


series_from_list = pd.Series(data=mylist)
series_from_array = pd.Series(data=myarr)
series_from_dict = pd.Series(data=mydict)

import helper_funcs as hf

hf.write_results_str("002", [series_from_list, series_from_array, series_from_dict])

