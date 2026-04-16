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
## Paste Error Log & It Will Analysis It !
![img](https://github.com/Saishekar17/self-healing-api-agent/blob/d337f2b8ce4119285942070032f2dc92896902f4/11.png)

## Restored History !
![img](https://github.com/Saishekar17/self-healing-api-agent/blob/613b4f802afbdeb6c32169a8225e3a69f70c1e4d/12.png)

## Fix Suggestions for Logs With Confidence Score !
![img](assets/screenshot.png)

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
