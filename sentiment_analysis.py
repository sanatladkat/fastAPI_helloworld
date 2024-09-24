from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the sentiment analysis model
model = pipeline("sentiment-analysis")

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict/")
def predict_sentiment(input: TextInput):
    result = model(input.text)
    return {"label": result[0]['label'], "score": result[0]['score']}
