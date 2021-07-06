import io

import requests
from PIL import Image

import streamlit as st

# interact with FastAPI endpoint
backend = "http://fastapi:8000/sentiment"


def process(text, server_url):

    r = requests.post(
        server_url, json={"text":text}, headers={"Content-Type": "application/json"}, timeout=8000)

    return r

# construct UI layout
st.title("Sentiment Analysis (7 Emotions)")

st.write(
    """Sentiment analysis based on the 1-P-3-ISEAR dataset.
         The front end is handled by streamlit and the backend with a FastAPI service.
         Visit 'http://127.0.0.1:8000/docs' for FastAPI documentation."""
)  # description and instructions

input_text = st.text_area('How are you feeling?')

if st.button("Get Emotion"):

    if input_text:
        sentiment = process(input_text, backend)
        st.write("Emotion detected:", sentiment.content.decode())

        if(sentiment.content.decode()=='Joy'):
            st.balloons()

    else:
        # handle case with no image
        st.write("Need a sentence to analyze")
