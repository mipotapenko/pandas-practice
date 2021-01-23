#!/bin/python3

# 1. How to import pandas and check the version?

import numpy as np
import pandas as pd

excercise = "001"
result_path = "ex" + excercise + "-result.txt"

pd.show_versions(as_json=result_path)

with open(result_path, "a") as result_file:
	result_file.write("\n")
	result_file.write(pd.__version__)
	result_file.write("\n")
	result_file.close()


