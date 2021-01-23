#!/bin/python3

# 5. How to assign name to the series’ index?

# Input

import pandas as pd

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

# Solution

ser.name = "alphabets"
# following line also works
# ser.rename("alphabets", inplace=True)

import helper_funcs as hf

hf.write_results_str("005", [ser])
