 
import os
from dotenv import load_dotenv

api_key = os.getenv("GEMINI_API_KEY")
eleven_api_key = os.getenv("ELEVEN_API_KEY")

print("OpenAI key loaded:", bool(openai_api_key))  # should print True if it's working

import gradio as gr
from rag_pipeline import get_rag_pipeline
from tts import speak

qa = get_rag_pipeline()

def ask_figure(question):
    response = qa.run(question)
    audio_file = speak(response)
    return response, audio_file

iface = gr.Interface(
    fn=ask_figure,
    inputs=gr.Textbox(label="Ask a historical figure..."),
    outputs=[gr.Textbox(label="Response"), gr.Audio(label="Voice")],
    title="🕰 Conversational Time Machine",
    description="Chat with a historical figure using LLM + RAG + TTS"
)

iface.launch()
