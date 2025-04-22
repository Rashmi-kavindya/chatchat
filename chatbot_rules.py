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

# Global stemmed keyword map
keyword_map = {
    stemmer.stem("leave"): "leave policy",
    stemmer.stem("vacation"): "leave policy",
    stemmer.stem("salary"): "salary day",
    stemmer.stem("pay"): "salary day",
    stemmer.stem("intern"): "internship duration",
    stemmer.stem("duration"): "internship duration",
    stemmer.stem("promotion"): "promotion",
    stemmer.stem("review"): "promotion",
    stemmer.stem("contact"): "contact hr",
    stemmer.stem("email"): "contact hr",
    stemmer.stem("hi"): "greeting",
    stemmer.stem("hello"): "greeting",
    stemmer.stem("bye"): "farewell",
    stemmer.stem("goodbye"): "farewell"
}

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
            return rules.get(intent)

    return "I'm sorry, I couldn't understand that. Can you please rephrase?"
