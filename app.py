# app.py

from flask import Flask, request, jsonify, render_template
import mysql.connector
from chatbot_rules import get_hr_response

app = Flask(__name__)

# Database Connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="chatbot"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = get_hr_response(user_input)

    # Save to DB
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_log (user_input, bot_response) VALUES (%s, %s)", (user_input, response))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
