#!/bin/python

# 6. How to get the items of series A not present in series B?

# Input

import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution

import numpy as np

ser_diff = pd.Series(np.setdiff1d(ser1, ser2))

# Solution on websit offers the following:
# ser1[~ser1.isin(ser2)]
# the "[]" is syntactic sugar for __get_item__. It can take a boolean array
# of the same length to determine which elements should be returned

import helper_funcs as hf
hf.write_results_str("006", [ser_diff])
