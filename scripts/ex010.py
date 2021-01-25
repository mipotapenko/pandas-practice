# 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?

import numpy as np
import pandas as pd
import helper_funcs as hf


# Input
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# Solution
top2 = list(ser.value_counts()[:2].index)
mod_ser = ser.where(lambda x: (x == top2[1]) | (x == top2[0]), "Other", axis=0)

# Website offers
# print("Top 2 Freq:", ser.value_counts())
# ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'

hf.write_results_str("010", [ser, top2, mod_ser])
