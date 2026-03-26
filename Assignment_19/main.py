'''
Assignment (21/03/2026)

Assignment Name : Build a Text Cleaner
Description : Write code to remove punctuation, 
lowercase text, remove stopwords and test it.
'''

import string

# Simple stopwords list
stopwords = ["is", "am", "are", "the", "a", "an", "and", "to", "in", "of", "for"]

def clean_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # 3. Remove stopwords
    words = text.split()
    cleaned_words = []
    
    for word in words:
        if word not in stopwords:
            cleaned_words.append(word)
    
    return " ".join(cleaned_words)

# Test the function
sentence = "This is a Simple Example, to test the Text Cleaner!"
result = clean_text(sentence)

print("Original:", sentence)
print("Cleaned:", result)