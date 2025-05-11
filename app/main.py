
import streamlit as st
from document_loader import load_documents
from vector_store import build_vector_store
from chat_engine import create_chatbot
from utils import format_response
import asyncio

# Fix async runtime error before Streamlit starts
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.run(asyncio.sleep(0))
@st.cache_resource
def init_chatbot():
    docs = load_documents("data/faqs.txt")
    vectordb = build_vector_store(docs)
    return create_chatbot(vectordb)

st.title("RAG-based FAQ Chatbot")

chatbot = init_chatbot()
user_input = st.text_input("Ask a question:")
if user_input:
    retrieved_docs = chatbot.retriever.invoke(user_input)  # Use invoke() instead of get_relevant_documents()
    
    # Extract only the correct response based on matching question
    answer = None
    for doc in retrieved_docs:
        lines = doc.page_content.split("\n")  # Split FAQs into lines
        for i in range(len(lines)):
            if user_input.lower() in lines[i].lower():  # Match question
                answer = lines[i + 1] if i + 1 < len(lines) else "Sorry, I couldn't find a direct answer."
                break
        if answer:
            break
    
    st.markdown(format_response(user_input, answer))
# if user_input:
#     response = chatbot.invoke({"query": user_input})

#     # Extract only the "result" key from the response dictionary
#     chatbot_answer = response.get("result", "Sorry, I couldn't find a relevant answer.")
    
#     st.markdown(format_response(user_input, chatbot_answer))
# if user_input:
#     # retrieved_context = " ".join([doc.page_content for doc in chatbot.retriever.get_relevant_documents(user_input)])
#     # print("Expected input keys:", chatbot.input_keys)
#     retrieved_context = chatbot.retriever.invoke(user_input)
#     response = chatbot.invoke({"query": user_input})
      
#     st.markdown(format_response(user_input, response))