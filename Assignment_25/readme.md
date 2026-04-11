# 📄 NLP Mini App – Keyword Extractor

# 📌 Overview

This project is a simple Natural Language Processing (NLP) web application that extracts important keywords from a given text. It uses the TF-IDF (Term Frequency–Inverse Document Frequency) technique to identify the most relevant words.

# 🎯 Features
Extracts top keywords from user input text
Removes common stopwords (like the, is, and)
User-friendly interface built with Streamlit
Adjustable number of keywords

# 🧰 Technologies Used
Python
Streamlit
Scikit-learn
NLTK

# ⚙️ Installation & Setup
1. Clone or Download the Project
git clone <your-repo-link>
cd nlp-mini-app
2. Install Required Libraries
pip install -r requirements.txt
3. Run the Application
streamlit run app.py

# 💡 How It Works
The user enters a block of text
The application processes the text by removing stopwords
TF-IDF is applied to calculate word importance
The top N keywords are displayed
📥 Example Input
Machine learning is a field of artificial intelligence that focuses on building systems that learn from data.
📤 Example Output
machine, learning, data, systems, artificial

# 📌 Project Structure
nlp-mini-app/
│
├── app.py
├── requirements.txt
└── README.md
🧠 Key Concept

TF-IDF helps in finding important words by:

Increasing weight for frequently used words in a document
Decreasing weight for commonly used words across all documents

# 📌 Outcome

Built a simple NLP application that extracts meaningful keywords from text and provides hands-on experience with text processing and machine learning techniques.