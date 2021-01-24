# 4. How to combine many series to form a dataframe?

# Input

import numpy as np
import pandas as pd

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution

import helper_funcs as hf

# The concat function can concatenate along a aprticular axis.
# Axis 1 in this case would be the axis that seperates series
# Axis 0 would concatenate the two series so that they are in the same column
df = pd.concat([ser1, ser2], axis=1, keys=["col1", "col2"])

hf.write_results_str("004", [df])
