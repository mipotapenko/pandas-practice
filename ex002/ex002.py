#!/bin/python3

# 2. How to create a series from a list, numpy array and dict?

# Input

import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# My Solution

import pandas as pd
import json

series_from_list = pd.Series(data=mylist)
series_from_array = pd.Series(data=myarr)
series_from_dict = pd.Series(data=mydict)

excercise = "002"
result_path = "ex" + excercise + "-result.txt"

with open(result_path, "w") as result_file:
	for series in [series_from_list, series_from_array, series_from_dict]:
		result_file.write(series.to_json)
		result_file.write("\n")
