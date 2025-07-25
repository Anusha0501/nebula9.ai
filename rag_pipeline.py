import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.schema import Document

CHROMA_PATH = "chroma_db"
DATA_DIR = "data"  # Folder containing all the .txt files

def setup_vectorstore():
    # Load all .txt files in the data directory
    all_documents = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(DATA_DIR, filename)
            loader = TextLoader(path)
            docs = loader.load()
            all_documents.extend(docs)

    if not all_documents:
        raise ValueError("No text documents loaded. Please check your data/ folder.")

    # Split into chunks
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    split_docs = splitter.split_documents(all_documents)

    # Create embeddings
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Save to Chroma
    vectorstore = Chroma.from_documents(documents=split_docs, embedding=embedding, persist_directory=CHROMA_PATH)
    vectorstore.persist()

    print(f"✅ Vectorstore created with {len(split_docs)} chunks")
    return vectorstore
