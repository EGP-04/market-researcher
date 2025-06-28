# 📊 Market Researcher – RAG Agent for Supply Hole Detection

A lightweight LLaMA-powered AI agent that answers natural language questions about mobile phone specifications using a CSV dataset, embeddings, and Retrieval-Augmented Generation (RAG). This is a prototype model for finding holes in the market for any product.

---

## 🚀 How to Run

install Ollama from the official site:

👉 [https://ollama.com/download](https://ollama.com/download)

pull the required models:

```bash
ollama pull mxbai-embed-large
ollama pull llama3
```

install required python libraries
```bash
pip install -r requirements.txt
```

run the fastAPI app
```bash
uvicorn fastAPI_:app --reload
```

now look at where the app is served and copy the corresponding localhost link to response in web.py
then run
```bash
streamlit run web.py
```
