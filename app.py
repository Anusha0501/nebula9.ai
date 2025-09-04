import streamlit as st
from dotenv import load_dotenv
import os

# LangChain components
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Coqui TTS for voice generation
from TTS.api import TTS

# --- 1. SETUP AND CONFIGURATION ---

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    st.error("Google API key not found. Please add it to your .env file.")
    st.stop()
    
# Define the path to your data folder
KNOWLEDGE_BASE_DIR = "data"

# --- 2. CACHED MODELS AND DATA ---

@st.cache_resource
def load_tts_model():
    """
    Loads and caches a Coqui TTS model suitable for a female British speaker.
    """
    try:
        # VCTK is a multi-speaker English dataset. We can pick a female speaker.
        return TTS("tts_models/en/vctk/vits")
    except Exception as e:
        st.error(f"Failed to load TTS model. Ensure you have a working internet connection. Error: {e}")
        st.stop()

@st.cache_resource
def create_rag_pipeline():
    """Loads data from the data directory, creates embeddings, and sets up the RAG pipeline."""
    if not os.path.exists(KNOWLEDGE_BASE_DIR):
        st.error(f"The 'data' directory was not found.")
        st.error("Please create a 'data' folder and add your .txt files to it.")
        st.stop()
        
    loader = DirectoryLoader(KNOWLEDGE_BASE_DIR, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if not documents:
        st.error(f"No .txt files found in the 'data' directory.")
        st.stop()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(docs, embedding_model)
    return vector_store.as_retriever()

# --- 3. LANGCHAIN CONVERSATIONAL CHAIN ---
# *** FIX: This entire block has been un-indented to the correct, top level. ***

def create_conversational_chain():
    """Creates the main LangChain conversational chain with the Queen's persona."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

    prompt = ChatPromptTemplate.from_template("""
    You are Queen Elizabeth II.
    Your knowledge is strictly limited to your lifetime, ending in September 2022.
    Your tone is formal, dignified, gracious, and composed. You speak using Received Pronunciation British English.
    You embody a strong sense of duty and public service. Refer to yourself as 'we' when speaking in a formal or official capacity.
    Answer the user's question based ONLY on the following provided context. Do not use any outside knowledge.
    If the context does not contain the answer, politely state, 'That is a matter upon which we do not typically comment,' or 'One's memory of that particular detail is not clear.'

    CONTEXT:
    {context}

    QUESTION:
    {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = create_rag_pipeline()
    return create_retrieval_chain(retriever, document_chain)

# --- 4. STREAMLIT UI ---
# *** FIX: This entire block has also been un-indented to the correct, top level. ***

st.set_page_config(page_title="Royal Audience", page_icon="👑")
st.title("👑 An Audience with The Queen")
st.subheader("You may ask a question of Her Majesty Queen Elizabeth II")

tts_model = load_tts_model()
chain = create_conversational_chain()

user_question = st.text_input("Your question for Her Majesty:")

if st.button("Request an Answer"):
    if user_question:
        with st.spinner("Awaiting Her Majesty's response..."):
            try:
                response = chain.invoke({"input": user_question})
                answer_text = response["answer"]
                
                st.markdown("---")
                st.subheader("Her Majesty's Response:")
                st.write(answer_text)

                audio_file_path = "response.wav"
                # Specifying a female speaker from the VCTK model.
                tts_model.tts_to_file(text=answer_text, file_path=audio_file_path, speaker='p225')

                st.audio(audio_file_path, autoplay=True)

            except Exception as e:
                st.error(f"An error occurred during response generation: {e}")
    else:
        st.warning("Please enter a question to receive a response.")

