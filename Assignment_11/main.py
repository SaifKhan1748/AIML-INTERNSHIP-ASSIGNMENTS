'''
Assignment (03/03/2026)

Assignment Name : Build Your First Dataset
Description : Create a dataset (e.g., study hours vs marks), 
identify features & labels, predict relationship.
'''

import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)
print(df)

'''
Feature (Input): Study_Hours
Label (Output): Marks
'''

import matplotlib.pyplot as plt

plt.scatter(df["Study_Hours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

"""
9 hours → Marks can be around 95–100
2.5 hours → Marks can be around 45–48
"""
