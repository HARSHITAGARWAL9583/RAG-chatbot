
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
def build_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(documents, embeddings)
    return db