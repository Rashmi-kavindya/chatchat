import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")  # Or Gemma-2b-it if 7b is unavailable

def chatbot(state: State):
    return {"messages": llm.invoke(state["messages"])}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")
graph = graph_builder.compile()

def get_ai_response(message):
    for event in graph.stream({"messages": [("user", message)]}):
        for value in event.values():
            return value["messages"].content
