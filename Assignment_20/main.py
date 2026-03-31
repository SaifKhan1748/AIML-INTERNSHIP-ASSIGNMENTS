"""
Assignment (24/03/2026)

Assignment Name :Word Importance Explorer
Description : Use TF-IDF on 5 documents and identify top keywords 
with explanation.
"""

documents = [
    "Machine learning is very useful for data science",
    "Data science uses machine learning algorithms",
    "Artificial intelligence and machine learning are related",
    "Python is widely used in data science",
    "Data analysis is important in machine learning"
]

from sklearn.feature_extraction.text import TfidfVectorizer

# Create TF-IDF model
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (words)
words = vectorizer.get_feature_names_out()

# Convert to array
import pandas as pd
df = pd.DataFrame(tfidf_matrix.toarray(), columns=words)

# Show top words for each document
for i in range(len(documents)):
    print(f"\nDocument {i+1} Top Words:")
    top_words = df.iloc[i].sort_values(ascending=False).head(3)
    print(top_words)

