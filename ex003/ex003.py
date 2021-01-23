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

df = ser.reset_index()

exercise = "003"
result_path = "ex" + exercise + "-result.txt"

with open(result_path, "w") as result_file:
	result_file.write(str(df))
	result_file.write("\n")


