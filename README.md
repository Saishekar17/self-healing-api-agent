# 🛠 Self-Healing API Agent (AI-Powered Debugging System)

An AI system that automatically detects API failures, analyzes logs, and suggests fixes using **LLMs, RAG (FAISS), and a self-learning feedback loop** — fully local with Ollama.

---

## 🚀 Features

- 🔍 AI-based error analysis (root cause detection)
- 🛠 Auto-generated fix suggestions (code patches)
- 🧠 Self-learning memory using FAISS (RAG)
- 📊 Confidence scoring for fixes
- 📚 Sidebar history with past errors & fixes
- ⚡ Fully local LLM using Ollama (no API cost)

---

## 🧱 Tech Stack

- Python
- FastAPI
- Streamlit
- Ollama (Local LLM)
- FAISS (Vector Database)
- Sentence Transformers

---

## ⚙️ Architecture

API Error → Analyzer → Fix Generator → RAG Memory → Confidence Scorer → UI

---

## 📸 UI Preview

![App Screenshot](assets/screenshot.png)

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt