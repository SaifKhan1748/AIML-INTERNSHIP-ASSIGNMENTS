'''
Assignment (03/04/2026)

Assignment Name : NLP Mini App
Description : Build a chatbot, fake news detector, or keyword extractor.
'''

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk # type: ignore
from nltk.corpus import stopwords # type: ignore

# Download stopwords (only first time)
nltk.download('stopwords')

# Function to extract keywords
def extract_keywords(text, num_keywords=5):
    stop_words = stopwords.words('english')  
    
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform([text])
    
    feature_array = vectorizer.get_feature_names_out()
    tfidf_scores = X.toarray()[0]
    
    # Get top keywords
    sorted_indices = tfidf_scores.argsort()[::-1]
    top_keywords = [feature_array[i] for i in sorted_indices[:num_keywords]]
    
    return top_keywords

# Streamlit UI
st.title("NLP Mini App - Keyword Extractor")

st.write("Enter text below and extract important keywords.")

user_input = st.text_area("Enter your text:")

num_keywords = st.slider("Number of keywords", 1, 10, 5)

if st.button("Extract Keywords"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        keywords = extract_keywords(user_input, num_keywords)
        
        st.subheader("Top Keywords:")
        for kw in keywords:
            st.write(f"• {kw}")