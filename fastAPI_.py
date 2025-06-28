from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

# ========== SETUP ==========
os.environ["LANGCHAIN_TRACING_V2"] = "false"

app = FastAPI()

# --- Load and chunk CSV ---
def csv_to_text_chunks(file_path):
    df = pd.read_csv(file_path, encoding="ISO-8859-1")
    df = df.drop(['Launched Price (Pakistan)', 'Launched Price (China)', 'Launched Price (USA)', 'Launched Price (Dubai)'], axis=1)
    chunks = []
    for i, row in df.iterrows():
        row_text = ". ".join(f"{col}: {val}" for col, val in row.items())
        chunks.append(row_text)
    return chunks

# --- Vector Store Setup ---
embedding = OllamaEmbeddings(model="mxbai-embed-large")
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

vector_store = Chroma(
    collection_name="mobile_data_rag",
    embedding_function=embedding,
    persist_directory=db_location
)

if add_documents:
    texts = csv_to_text_chunks("mobile_dataset.csv")
    documents = [Document(page_content=t) for t in texts]
    ids = [str(i) for i in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# --- LLM Setup ---
llm = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about mobile phones.

Here is some relevant information from the dataset:
{info}

Now answer this question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

# ========== FASTAPI ROUTE ==========

class Query(BaseModel):
    question: str

@app.post("/run-agent")
def run_agent(query: Query):
    info = retriever.invoke(query.question)
    result = chain.invoke({
        "info": info,
        "question": query.question
    })
    return {"answer": result}