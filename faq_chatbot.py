import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

faq_df = pd.read_csv("faq_data.csv")

# Function to match user's query with the FAQ questions
def get_answer(user_query, threshold=0.1):
    # Create a TfidfVectorizer to convert text to vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Combine user query with all FAQ questions for comparison
    faq_questions = faq_df['Question'].tolist()
    faq_questions.append(user_query)  # Append the user's query to the list
    
    # Convert text to tf-idf matrix
    tfidf_matrix = vectorizer.fit_transform(faq_questions)
    
    # Calculate cosine similarity between the user's query and all FAQ questions
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Filter results based on the threshold for similarity
    matching_results = []
    for idx, sim_score in enumerate(cosine_sim[0]):
        if sim_score >= threshold:
            question = faq_df.iloc[idx]['Question']
            answer = faq_df.iloc[idx]['Answer']
            matching_results.append((question, answer, sim_score))
    
    # Sort the matching results by the similarity score
    matching_results.sort(key=lambda x: x[2], reverse=True)
    
    return matching_results

# Streamlit interface
st.title("FAQ Chatbot")

# Create a text input field for user query
user_query = st.text_input("Ask your question:")

if user_query:
    answers = get_answer(user_query)  # Get matching answers from the FAQ dataset
    
    if answers:
        for idx, (question, answer, score) in enumerate(answers, 1):
            st.write(f"**Question {idx}:** {question}")
            st.write(f"**Answer {idx}:** {answer}")
    else:
        st.write("Sorry, I couldn't find any matching FAQs.")
