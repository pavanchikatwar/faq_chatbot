# FAQ Chatbot for E-commerce Website

## Project Overview
This **FAQ chatbot** is designed to automate the process of answering frequently asked questions on an e-commerce website, offering quick, accurate, and helpful responses to customers. The chatbot is integrated with a simple and easy-to-use web interface, providing 24/7 support for users visiting the website, improving customer experience and reducing the burden on customer service teams.

## Features
- **Automated FAQ Responses**: Provides instant answers to common questions like shipping, return policies, and product details.
- **Natural Language Understanding (NLU)**: The chatbot uses pre-trained NLP models to understand user queries even if they are phrased differently than the FAQs.
- **Web Interface**: A chat interface that is simple to interact with, allowing users to type questions and receive answers in real-time.
- **Dynamic Content**: The system allows for easy updates to the FAQ database, ensuring the chatbot answers questions based on the most current information.
- **Fallback Mechanism**: In case the chatbot cannot answer a question, it provides a default response or suggests contacting customer support.

## Python Libraries Used:

### Pandas (`pd`)
- Used to read and manipulate the FAQ data stored in a CSV file (`faq_data.csv`).

### Scikit-learn
- **`TfidfVectorizer`**: Converts text data (FAQ questions) into numerical vectors for similarity computation.
- **`cosine_similarity`**: Measures similarity between the user's query and FAQ questions using cosine similarity scores.

### Streamlit (`st`)
- Provides an interactive web interface for the chatbot, enabling users to input questions and receive answers dynamically.


## Functionality
1. **User Query Input**: Users can type questions into the chatbot interface.
2. **Response Generation**: The chatbot uses an NLP model to process the question and return an appropriate answer from the FAQ database.
3. **Error Handling**: If the chatbot cannot provide a response, it suggests possible next steps, such as checking the FAQ page or contacting customer support.
4. **Updates and Maintenance**: The FAQ content can be easily modified by updating the database, which ensures the chatbot provides up-to-date information.

## Requirements
The following dependencies are required to run the project:

- Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

- To run the app, execute:
    ```bash
    streamlit run faq_chatbot.py
    ```

## Conclusion
The **FAQ chatbot** offers a great starting point for integrating AI-powered customer support into an e-commerce website. By providing automated answers to frequently asked questions, the chatbot enhances user experience while reducing the load on human support agents. The chatbot is easy to integrate, update, and scale, making it a powerful tool for any e-commerce platform.



![Screenshot (123)](https://github.com/user-attachments/assets/08d87c5c-82c4-4dec-a921-5816ccd9d7ca)

---

![Screenshot (124)](https://github.com/user-attachments/assets/a35f12f4-7ccd-4a32-9f50-d8fb8e5e62a1)

---

![Screenshot (121)](https://github.com/user-attachments/assets/179e3c80-0c1e-40d4-a00f-61ce85a85158)

---

![Screenshot (122)](https://github.com/user-attachments/assets/a34d6e3f-7127-4ae8-b25d-b175c9beb75e)



