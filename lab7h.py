# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules.

# TO DO 2: Draw histogram of the data from movies database.

# TO DO 3: Perform the operations provided in readme.md file on this data.

# TO DO 4: Run the script.
import pandas as pd
import matplotlib.pyplot as plt
movies=pd.read_csv("https://github.com/itiievskyi/IMDB-Top-250/blob/master/imdb_top_250.csv")
years=movies["Year"].copy()
years_sort=years.sort()
print(years_sort)
sort_unique_years=years_sort.unique()
print(sort_unique_years)
years_occur=years_sort.occur()
print(years_occur)
years_occur=years_occur.head(10)
plt.title('Data from Movies Database')
plt.xlabel('The Number of Years')
plt.ylabel('The Number of Movies')
plt.show()

