# 9. How to get frequency counts of unique items of a series?

import numpy as np
import pandas as pd
import helper_funcs as hf

# Input
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# Solution

counts = ser.value_counts()
hf.write_results_str("009", [ser, counts])
