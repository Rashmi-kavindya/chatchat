# chatbot_rules.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')

rules = {
    "leave policy": "Our leave policy includes 14 annual leave days and 10 casual leave days.",
    "salary day": "Salaries are processed on the 25th of every month.",
    "internship salary": "Interns receive their salary on the 10th of every month.",
    "internship duration": "Internships typically last for 6 months.",
    "promotion": "Promotions depend on performance reviews held bi-annually.",
    "contact hr": "You can contact HR at hr@foresight.com or ext 102.",
    "greeting": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day ahead!"
}

stemmer = PorterStemmer()

def get_hr_response(message):
    message = message.lower()
    tokens = word_tokenize(message)
    stemmed = [stemmer.stem(token) for token in tokens]

    # Custom keyword-intent mapping
    keyword_map = {
        "leave": "leave policy",
        "vacation": "leave policy",
        "salary": "salary day",
        "pay": "salary day",
        "intern": "internship salary" if "salary" in stemmed else "internship duration",
        "duration": "internship duration",
        "promot": "promotion",
        "review": "promotion",
        "contact": "contact hr",
        "email": "contact hr",
        "hi": "greeting",
        "hello": "greeting",
        "bye": "farewell",
        "goodbye": "farewell"
    }

    for word in stemmed:
        if word in keyword_map:
            intent = keyword_map[word]
            return rules.get(intent)

    return "I'm sorry, I couldn't understand that. Can you please rephrase?"
