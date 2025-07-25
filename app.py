# app.py

import os
import streamlit as st
from dotenv import load_dotenv
from tts import speak_text
from rag_pipeline import setup_vectorstore, query_db
import google.generativeai as genai

# 🔐 Load API keys from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 🎯 Initialize LLM (Gemini Pro 1.5 Flash)
model = genai.GenerativeModel("gemini-pro")

# 🧠 Setup RAG vectorstore
vectorstore = setup_vectorstore()

# 🗣️ App UI
st.set_page_config(page_title="Elizabeth Time Machine", page_icon="🕰️")
st.title("👸🏼 Elizabeth Time Machine")
st.caption("Travel back in time to talk with Queen Elizabeth I (via AI)")

# 🎤 User input
query = st.text_input("Ask Elizabeth a question", placeholder="What was your childhood like?")

if st.button("Ask"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking like a Queen..."):
            # RAG step
            context = query_db(query, vectorstore)

            # Prompt
            prompt = f"""
You are Queen Elizabeth I speaking to a curious visitor from the future.
Respond in a regal, poetic tone using this context when needed:

Context:
{context}

User Question:
{query}
"""
            # Generate LLM response
            response = model.generate_content(prompt)
            answer = response.text.strip()

            # 🎤 Show + Speak answer
            st.markdown(f"**Elizabeth:** {answer}")
            speak_text(answer)
