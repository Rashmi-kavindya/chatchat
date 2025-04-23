import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="Gemma-2b-it"
)

def get_ai_response(user_input):
    try:
        message = HumanMessage(content=user_input)
        response = llm.invoke([message])
        return response.content
    except Exception as e:
        return "Sorry, I couldn’t process that right now."