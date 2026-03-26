'''
Assignment (24/02/2026)
Assignment Name : Dataset Detective
Description : Load a dataset, display top rows, 
find highest value column, count missing values, share 5 insights.
'''

import pandas as pd

# Load dataset
data = pd.read_csv("Salary_Data.csv")

# Display top 5 rows
print("Top 5 Rows:")
print(data.head())

# Find column with highest maximum value
max_values = data.max(numeric_only=True)
highest_column = max_values.idxmax()

print("\nColumn with Highest Value:", highest_column)
print("Highest Value:", max_values.max())

# Count missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())