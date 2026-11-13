# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.

# TO DO 2: Create a series according to instructions given in readme.md file.

# TO DO 3: Perform the operations on this series given in readme.md file.

# TO DO 4: Run the script.
import pandas as pd
grade_list=["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
grades=pd.Series(grade_list,index=["F", "D", "C", "B", "A", "A+"])
# Printing the whole series
print(grades)
# Print values for index C and A+
print(grades.loc[["C","A+"]])
# Print value 60-69 directly
print(grades.iloc[2])
print(grades["C"])
# * operation on Series
print(grades*3)

