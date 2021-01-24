# 7. How to get the items not common to both series A and series B?

# Input

import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution

combined_series = pd.concat([ser1[~ser1.isin(ser2)], ser2[~ser2.isin(ser1)]], axis=0)

# Website suggests using 1d intersection and 1d difference to form the final series.
# The difference between my solution and the website is theirs preserves indices of the union...
# while mine preserves the indices of the original list

import helper_funcs as hf

hf.write_results_str("007", [combined_series])
