import streamlit as st
import requests

st.title("Text Sentiment & Timestamp")

text = st.text_area("Enter text to analyze:")
if st.button("Analyze"):
    response = requests.post("http://flask-api:5000/analyze", json={"text": text})
    if response.ok:
        data = response.json()
        st.write("**Input:**", data["input"])
        st.write("**Sentiment:**", data["sentiment"])
        st.write("**Timestamp (UTC):**", data["timestamp"])
    else:
        st.error("Error: " + response.text)
