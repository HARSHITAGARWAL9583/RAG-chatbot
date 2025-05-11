
from langchain.chains import RetrievalQA
from transformers import pipeline
import logging
from langchain_huggingface import HuggingFacePipeline
logging.basicConfig(level=logging.DEBUG)

def get_llm():
    pipe = pipeline("text-generation", model="gpt2", max_length=200)
    return HuggingFacePipeline(pipeline=pipe)
def create_chatbot(vector_db):
    llm = get_llm()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vector_db.as_retriever(), return_source_documents=True)
    return qa