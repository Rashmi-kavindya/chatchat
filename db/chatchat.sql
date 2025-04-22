CREATE DATABASE IF NOT EXISTS hr_chatbot;
USE chatbot;

CREATE TABLE chat_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_input TEXT,
    bot_response TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
