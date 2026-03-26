'''
Assignment (11/03/2026)

Assignment Name : Customer Segmentation
Description : Perform K-Means clustering on a mall dataset 
and describe customer groups.
'''

import pandas as pd

data = {
    "Income": [15, 16, 17, 50, 55, 60, 90, 95, 100],
    "Spending": [20, 25, 30, 50, 55, 60, 80, 85, 90]
}

df = pd.DataFrame(data)


from sklearn.cluster import KMeans

# Select features
X = df[["Income", "Spending"]]

# Create model (3 clusters)
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Add cluster labels
df["Cluster"] = kmeans.labels_

print(df)

import matplotlib.pyplot as plt

plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.show()