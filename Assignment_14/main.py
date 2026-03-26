'''Assignment (10/03/2026)

Assignment Name : Spam Classifier Thinking
Description : Design a spam detection system: features, 
data needed, possible mistakes.
'''

# Simple dataset
messages = [
    "win money now",
    "free offer click here",
    "hello how are you",
    "let's study together",
    "urgent prize claim now"
]

labels = ["spam", "spam", "ham", "ham", "spam"]

# Convert text into numbers (very basic)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Step 2: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 3: Test with new message
test_msg = ["free money offer"]
test_vector = vectorizer.transform(test_msg)

prediction = model.predict(test_vector)

print("Message:", test_msg[0])
print("Prediction:", prediction[0])