import os
from pathlib import Path
from typing import List

try:
    from langchain_community.document_loaders import TextLoader
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.vectorstores import Chroma
except ImportError:  # Backward compatibility for older langchain versions
    from langchain.document_loaders import TextLoader
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.vectorstores import Chroma

from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document

CHROMA_PATH = "chroma_db"
DATA_DIR = "data"


def _load_documents() -> List[Document]:
    all_documents: List[Document] = []
    data_path = Path(DATA_DIR)

    if not data_path.exists():
        raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")

    for path in sorted(data_path.glob("*.txt")):
        loader = TextLoader(str(path), encoding="utf-8")
        docs = loader.load()
        all_documents.extend(docs)

    if not all_documents:
        raise ValueError("No text documents loaded. Please check your data/ folder.")

    return all_documents


def _build_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def setup_vectorstore() -> Chroma:
    """Load an existing vector store if available; otherwise build it."""
    embeddings = _build_embeddings()

    if os.path.isdir(CHROMA_PATH) and os.listdir(CHROMA_PATH):
        return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    all_documents = _load_documents()
    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    split_docs = splitter.split_documents(all_documents)

    vectorstore = Chroma.from_documents(
        documents=split_docs,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
    )
    vectorstore.persist()
    return vectorstore


def query_db(query: str, vectorstore: Chroma, k: int = 4) -> str:
    results = vectorstore.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in results)
