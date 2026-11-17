# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

# TO DO 1: Create dataframe from provided dictionaries in readme.md file.
import pandas as pd
dict1={"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
dict2={"Okra": 'Thin', 'Potato': 'blob', 'Radish': 'Round'}
dict3={'Apple': 2.1, 'Okra': 3.5, 'Carrot': 1.3, 'Potato': 2.0, 'Radish': 3.0}

fruit={"color":dict1,"shape":dict2,"size":dict3}
df=pd.DataFrame(fruit)
print("DataFrame df")
print(df)

# TO DO 2: create a data frame provided in dataframe.jpg file.
dict4={"Student Name": ["A","B","C","D"],"Student Marks": [22,344,55,77]}
classes={"Math":dict4,"English":dict4,"Urdu":dict4,"Science":dict4}
df2=pd.DataFrame(classes)
print("DataFrame df2")

# TO DO 3: Run the script.
