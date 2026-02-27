
# 👑 Conversational Time Machine – Queen Elizabeth II 

_“I declare before you all that my whole life shall be devoted to your service…”_

A voice-driven, AI-powered interface that allows you to have natural, historically grounded conversations with **Queen Elizabeth II**, focused on her early life (from birth in 1926 up to her coronation in 1953).

![images (3)](https://github.com/user-attachments/assets/9b4dc264-1f9e-4739-af30-dbe796ac68a7)

---

## 🎬 Inspiration

After watching *The Crown* and witnessing the quiet strength and leadership of Queen Elizabeth II, I was moved to build a project that captures her voice, her memory, and her legacy in a respectful and engaging way. As a history enthusiast and AI developer, I saw the potential for blending **LLMs**, **retrieval-based learning**, and **text-to-speech** to make history feel personal and alive.

---

## 🧠 What Is This?

An interactive chatbot that brings a historical figure to life using:

- 📚 **RAG (Retrieval-Augmented Generation)** over real speeches, public letters & Wiki archives
- 🤖 **Gemini 1.5 Flash** for context-aware, time-constrained LLM generation
- 🗣️ **Coqui TTS (Open Source)** for rich voice synthesis (British female voice)
- 💻 **Streamlit** frontend for real-time chat with voice output

---

## 🎯 Project Scope

This project focuses **only** on the early life of Queen Elizabeth II, including:

- Her childhood and royal upbringing
- Experiences during WWII
- Her father's death and becoming heir presumptive
- Her coronation in 1953

<img width="715" height="665" alt="Screenshot 2025-07-25 at 19 29 05" src="https://github.com/user-attachments/assets/bcf061d2-92bf-4166-b9f9-b689e3b35554" />

---

## 🛠️ Tech Stack

| Component         | Tool / API                        |
|------------------|-----------------------------------|
| Language Model    | Gemini 1.5 Flash (Google AI)  |
| Retrieval         | ChromaDB + SentenceTransformers   |
| Prompting Engine  | LangChain                         |
| Voice Synthesis   | Coqui TTS (en speaker)            |
| Frontend UI       | Streamlit                         |
| Deployment        | Streamlit Cloud                   |

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Anusha0501/nebula9.ai.git
cd nebula9.ai

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys (Gemini)
cp .env.example .env
# Then edit .env and fill in your Gemini API key

# 5. Run the app
streamlit run app.py
```


## 🗃️ Project Structure

```bash
nebula9ai/
├── data/                    # Historical text (e.g., speeches, letters)
├── embeddings/              # Chroma vector store
├── prompts.py               # Persona + context-based prompting logic
├── rag_pipeline.py          # RAG retrieval pipeline
├── tts.py                   # Coqui TTS logic
├── app.py                   # Main Streamlit interface
├── requirements.txt
└── .env.example             # Gemini API keys (no Google TTS required)
```

---


## 🧪 Production Readiness Checklist

- Set `GEMINI_API_KEY` and (optionally) `GEMINI_MODEL` in your deployment environment.
- Keep `data/*.txt` bundled in the deployed artifact for retrieval to work.
- Persist `chroma_db/` on disk (or pre-build during image build) to avoid cold-start embedding time.
- Streamlit Cloud / container deployments should expose only the Streamlit port and disable shell access.
- Add CI checks (`python -m py_compile app.py rag_pipeline.py tts.py prompts.py`) before deploy.

## 🧪 Sample Prompts You Can Ask

> 💬 “What was your role during the Second World War?”
> 💬 “How did your father’s death affect your life?”
> 💬 “What did you feel on coronation day?”
> 💬 “What was your relationship with Winston Churchill like?”

⛔ Questions like “What do you think of Prince Harry?” will be politely declined with time-accurate messaging.

---

## ✨ Features

✅ **Time-Constrained LLM** — Response limited to pre-1953 history
✅ **Context-Rich Responses** — RAG over historical texts and speeches
✅ **Voice Responses** — Realistic British voice via Coqui TTS
✅ **Elegant Streamlit UI** — Timeline-aware, minimalist design
✅ **Open Source Friendly** — Fully local voice synthesis

---

## 🏛️ Real-World Use Cases

* 🎓 **Education**: Bring historical figures into classrooms
* 🏛️ **Museums**: Create interactive AI-powered exhibits
* 🎙️ **Media & Creators**: Generate character interviews or period storytelling
* 💡 **Research**: Explore persona-grounded LLM alignment challenges


