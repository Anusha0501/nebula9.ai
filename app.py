import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

from prompts import build_elizabeth_prompt
from rag_pipeline import query_db, setup_vectorstore
from tts import synthesize_speech

load_dotenv()

st.set_page_config(page_title="Elizabeth Time Machine", page_icon="🕰️")
st.title("👸🏼 Elizabeth Time Machine")
st.caption("Travel back in time to talk with Queen Elizabeth II (via AI)")

api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

if not api_key:
    st.error("GEMINI_API_KEY is not configured. Add it to your environment or .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name)


@st.cache_resource
def get_vectorstore():
    return setup_vectorstore()


vectorstore = get_vectorstore()
query = st.text_input("Ask Elizabeth a question", placeholder="What was your childhood like?")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking like a Queen..."):
            context = query_db(query, vectorstore)
            prompt = build_elizabeth_prompt(context, query)
            response = model.generate_content(prompt)
            answer = response.text.strip()

        st.markdown(f"**Elizabeth:** {answer}")
        audio_path = synthesize_speech(answer)
        st.audio(str(audio_path), format="audio/wav")
