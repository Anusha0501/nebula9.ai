
# 👑 Conversational Time Machine – Queen Elizabeth II (1926–1953)

_“I declare before you all that my whole life shall be devoted to your service…”_  
A voice-based AI experience that lets you have a natural, historically grounded conversation with **Queen Elizabeth II**, focused on her life until her coronation in **1953**.

![images (3)](https://github.com/user-attachments/assets/9b4dc264-1f9e-4739-af30-dbe796ac68a7)

---

## 🧠 What is This?

An interactive chatbot that brings a historical figure to life using:
- 📚 **RAG (Retrieval-Augmented Generation)** from real speeches, letters & wiki
- 🤖 **Gemini Pro 1.5 Flash** for context-aware, time-bounded LLM responses
- 🗣️ **Google Cloud TTS** for voice cloning (British female voice)
- 🧱 **Streamlit UI** for real-time interaction with voice output

---

### 🤖 Why This Is a Real-World Problem

* Museums could use it to **educate visitors interactively**.
* Schools could use it for **history lessons with AI-driven tutors**.
* Content creators could simulate **“interviews” with historical figures**.
* It combines the real challenges of:

  * **AI alignment (staying in-character)**
  * **Data retrieval (RAG)**
  * **Voice tech (TTS or voice cloning)**
  * **UI/UX design for natural conversation**

---

## 🎯 Focus of the Project

This project focuses **only on the early life of Queen Elizabeth II** (from birth in 1926 to her coronation in 1953), offering:
- Historical context
- Personalized tone and voice
- Filtered knowledge (no modern or post-1953 events)

---

## 🛠️ Tech Stack

| Component            | Tool / API Used                      |
|---------------------|--------------------------------------|
| Language Model       | Gemini Pro 1.5 Flash (Google AI)     |
| Retrieval (RAG)      | ChromaDB + SentenceTransformers      |
| Prompting Engine     | LangChain                            |
| Voice Synthesis      | Google Cloud TTS (en-GB-Wavenet-C)   |
| UI Framework         | Streamlit                            |
| Deployment           | Streamlit Cloud                      |

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Anusha0501/nebula9.ai.git
cd nebula9.ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API keys
cp .env.example .env
# Then edit .env to include your Google + Gemini API keys

# 4. Run the Streamlit app
streamlit run streamlit_app.py
````

---

## 🗃️ Project Structure

```bash
├── data/                    # Historical text (lilibet.txt)
├── embeddings/              # Chroma vector store
├── rag_pipeline.py          # Semantic search over historical content
├── prompting.py             # Persona + context-based prompting logic
├── tts.py                   # Text-to-Speech (voice synthesis)
├── streamlit_app.py         # Main Streamlit frontend
├── requirements.txt
└── .env.example             # API keys (Gemini, Google TTS)
```

---

## 🧪 Sample Prompts You Can Ask

> 💬 “What was your role during the Second World War?”
> 💬 “How did you feel when your father became King?”
> 💬 “Tell me about your coronation day.”
> 💬 “What was your relationship with Winston Churchill like?”

⛔ Questions like “What do you think of Prince Harry?” will be rejected with polite, time-accurate responses.

---

## ✨ Features

* 🧠 **Time-Constrained LLM** → No post-1953 knowledge
* 🧬 **RAG Context Injection** → Real historical sources only
* 🔊 **Voice Response Output** → Text-to-speech with British accent
* 🖼️ **Elegant UI** → Clean Streamlit layout with timeline awareness
* 🧠 **Assumption Handling** → Simulates the Queen’s memory & style


