'''
Assignment (26/02/2026)
Assignment Name : Data Doctor
Description : Clean a dataset by handling missing values, 
removing duplicates, standardizing text, and explain why cleaning matters.
'''

import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ali", "John", None],
    "Age": [20, 21, 20, None, 22],
    "City": ["Mumbai", "Delhi", "Mumbai", "delhi", "Chennai"]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Fill missing Age with average
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Fill missing Name with 'Unknown'
df["Name"].fillna("Unknown", inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

df["City"] = df["City"].str.lower()
df["Name"] = df["Name"].str.capitalize()

print("\nCleaned Data:\n", df)


# Explanation of why cleaning matters:

'''
- Dirty data gives wrong results
- Missing values can affect calculations
- Duplicate data creates bias
- Inconsistent text makes grouping difficult

👉 Clean data = better analysis + better model performance
'''