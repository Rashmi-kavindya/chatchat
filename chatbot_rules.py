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
    "greeting_1": "Hello! How can I assist you today?",
    "greeting_2": "Hi again! How can I help you?",
    "greeting_3": "You seem friendly today 😊 What can I do for you?",
    "greeting_4": "You've said hi quite a bit! 😄 What would you like to know?",
    "farewell": "Goodbye! Have a great day ahead!"
}

stemmer = PorterStemmer()

# Define intent keywords as groups
intent_keywords = {
    "leave policy": ["leave", "vacation"],
    "salary day": ["salary", "pay"],
    "internship duration": ["intern", "duration"],
    "promotion": ["promotion", "review"],
    "contact hr": ["contact", "email"],
    "greeting": ["hi", "hello"],
    "farewell": ["bye", "goodbye"]
}

# Build stemmed keyword_map dynamically
keyword_map = {}
for intent, keywords in intent_keywords.items():
    for word in keywords:
        keyword_map[stemmer.stem(word)] = intent


# To track how often each intent has been used
intent_counter = {}

def get_hr_response(message):
    message = message.lower()
    tokens = word_tokenize(message)
    stemmed = [stemmer.stem(token) for token in tokens]

    # Special case: intern + salary
    if stemmer.stem("intern") in stemmed and stemmer.stem("salary") in stemmed:
        return rules["internship salary"]

    for word in stemmed:
        if word in keyword_map:
            intent = keyword_map[word]

            # Count the intent use
            intent_counter[intent] = intent_counter.get(intent, 0) + 1
            count = intent_counter[intent]

            # Dynamic responses for greetings
            if intent == "greeting":
                if count == 1:
                    return rules.get("greeting_1")
                elif count == 2:
                    return rules.get("greeting_2")
                elif count == 3:
                    return rules.get("greeting_3")
                else:
                    return rules.get("greeting_4")

            return rules.get(intent)

    return "I'm sorry, I couldn't understand that. Can you please rephrase?"
