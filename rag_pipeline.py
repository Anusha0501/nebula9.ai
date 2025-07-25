# rag_pipeline.py

import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.schema import Document

CHROMA_PATH = "chroma_db"
DATA_PATH = "data/figure.txt"  # 📁 Place biography/context file here

# 🔍 Setup vectorstore from data file
def setup_vectorstore():
    # Load data
    loader = TextLoader(DATA_PATH)
    documents = loader.load()

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.split_documents(documents)

    # Embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Save to ChromaDB
    vectorstore = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=CHROMA_PATH)
    vectorstore.persist()
    return vectorstore

# 🔎 Query vectorstore for relevant context
def query_db(query, vectorstore, k=3):
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([doc.page_content for doc in docs])
