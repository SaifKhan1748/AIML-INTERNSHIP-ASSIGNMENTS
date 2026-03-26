from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = {
    "A": [5, 1, 0],
    "B": [4, 1, 1],
    "C": [1, 5, 4],
    "D": [5, 0, 0]
}

df = pd.DataFrame(data, index=["Action", "Comedy", "Romance"])

similarity = cosine_similarity(df.T)
print(similarity)