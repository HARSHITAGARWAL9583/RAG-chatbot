# RAG-based Chatbot 

This is a simple Retrieval-Augmented Generation (RAG) chatbot that uses open-source tools only.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
streamlit run app/main.py
```

## Features
- Uses FAISS for retrieval
- Uses GPT-2 for generation
- Embedding via sentence-transformers (free)
- Domain: FAQs / customer support
