from sentiment_analyser import analyzer
from starlette.responses import PlainTextResponse
from pydantic import BaseModel

from fastapi import FastAPI

# model = get_analyzer()

app = FastAPI(
    title="Emotion Detection",
    description="""Emotion analysis based on input sentence.
                           Visit this URL at port 8501 for the streamlit interface.""",
    version="0.0.1",
)

class Text(BaseModel):
    text: str

@app.post("/sentiment")
def text_handler(text: Text):
    """Get emotion analysis from NLP model"""
    print(text)
    emotion = analyzer(text)
    return PlainTextResponse(emotion)
