# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.

# TO DO 2: Perform the operations provided in readme.md file on this data frame.

# TO DO 3: Run the script.
import pandas as pd
movies=pd.read_csv("C:\Users\roopr\Downloads\imdb_top_250.csv")
print(movies.head(10))
print(movies.tail(10))
print(movies.columns)
print("Earliest movie":movies['Year'].min())
print(movies['Genre'].unique())
list_not_usa_movies=movies[movies["Origin"]!="USA"]
print(len(list_not_usa_movies))

