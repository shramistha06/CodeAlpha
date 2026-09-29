import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK data
nltk.download('punkt')

# FAQ Dataset
faq_data = {
    "What is AI?": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "What is Python?": "Python is a popular programming language used in AI, web development, and data science.",
    "What is NLP?": "NLP stands for Natural Language Processing, a field that helps computers understand human language.",
    "What is Data Science?": "Data Science involves extracting insights and knowledge from data."
}

# Questions and Answers
questions = list(faq_data.keys())
answers = list(faq_data.values())

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def chatbot(user_query):
    # Convert user query to vector
    query_vector = vectorizer.transform([user_query])

    # Calculate similarity
    similarity_scores = cosine_similarity(query_vector, question_vectors)

    # Get best match
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    if best_score > 0.2:
        return answers[best_match_index]
    else:
        return "Sorry, I couldn't find a matching answer."

# Chat Loop
print("FAQ Chatbot (Type 'exit' to quit)")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot(user_input)
    print("Chatbot:", response)