# 📊 Market Researcher – RAG Agent for Mobile Dataset

A lightweight LLaMA-powered AI agent that answers natural language questions about mobile phone specifications using a CSV dataset, embeddings, and Retrieval-Augmented Generation (RAG).

---

## 🚀 How to Run

### 1. Download & Start Ollama
Install Ollama from the official site:

👉 [https://ollama.com/download](https://ollama.com/download)

Then pull the required models:

```bash
ollama pull mxbai-embed-large
ollama pull llama3

pip install -r requirements.txt

uvicorn fastAPI_:app --reload

```

now look at where the app is served and copy the corresponding localhost link to response in web.py
then run

```bash
streamlit run web.py
```
