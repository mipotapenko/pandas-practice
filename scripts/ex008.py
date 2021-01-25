# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?

import numpy as np
import pandas as pd
import helper_funcs as hf

# Input
ser = pd.Series(np.random.normal(10, 5, 25))

# Solution
summary_series = ser.describe()

# The Website suggests
# print(np.percentile(ser, q=[0, 25, 50, 75, 100]))
# Also possible is
# print(ser.quantile([0, 0.25, 0.5, 0.75, 1.0]))
print(summary_series)
hf.write_results_str("008", [ser, summary_series])
