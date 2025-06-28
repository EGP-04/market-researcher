# market-researcher

## How to run it 
Download ollama from https://ollama.com/download
ollama pull mxbai-embed-large
ollama pull llama3

install the dependencies in requirements.txt

uvicorn fastAPI_:app --reload    

now take served localhost link and paste it in web.py response part

streamlit run web.py

