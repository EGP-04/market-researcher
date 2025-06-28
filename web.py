# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="Mobile RAG Agent", layout="centered")
st.title("Mobile Phones Q&A Agent")

st.markdown("""
        This app allows you to ask questions about mobile phones and find out umbrella of mobiles that have not been made available in the market yet.
""")

question = st.text_input("Enter your question:")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/run-agent",  # Change to deployed URL if needed
                json={"question": question},
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            st.success("Answer:")
            st.write(result["answer"])
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to the backend: {e}")