#!/bin/python

# 7. How to get the items not common to both series A and series B?

# Input

import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution

print(ser1.compare(ser2, align_axis=0))
