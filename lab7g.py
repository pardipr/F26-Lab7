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
import matplotlib.pyplot as plt
movies=pd.read_csv("https://github.com/itiievskyi/IMDB-Top-250/blob/master/imdb_top_250.csv")
print("The Summary of the Data")
print(movies.describe())
print("The First 10 Rows")
print(movies.head(10))
print("The Last 10 Rows")
print(movies.tail(10))
print(movies.columns)
print("Earliest movie":movies['Year'].min())
print("Latest movie":movies['Year'].max())
print("Unique Values in the Genre")
print(movies['Genre'].unique())
list_not_usa_movies=movies[movies["Origin"]!="USA"]
print("The Number of Movies that are not Made in the USA are:",len(list_not_usa_movies))
ten_highest_rated_movies=movies

