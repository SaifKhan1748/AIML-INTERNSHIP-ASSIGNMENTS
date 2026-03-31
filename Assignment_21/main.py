"""
Assignment (26/03/2026)

Assignment Name : Movie Review Analyzer
Description : Build a simple sentiment analyzer and test on 5 reviews.
"""

reviews = [
    "The movie was amazing and full of suspense",
    "I really loved the acting and storyline",
    "The film was boring and too long",
    "Worst movie I have ever seen",
    "It was okay, not that great"
]

from textblob import TextBlob   # type: ignore

for i, review in enumerate(reviews):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"
    
    print(f"Review {i+1}: {review}")
    print(f"Sentiment: {sentiment}")
    print("-" * 50)

