#!/bin/python3

# 3. How to convert the index of a series into a column of a dataframe?

# Input

import numpy as np
import pandas as pd

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# My Solution

import sys
print(sys.path)

import helper_funcs as hf

df = ser.reset_index()

hf.write_results_str("003", [df])




