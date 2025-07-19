from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

def create_vector_db(file_path: str, persist_path="faiss_index"):
    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(persist_path)

def get_rag_pipeline(persist_path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(persist_path, embeddings)
    
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo")
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain
