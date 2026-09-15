from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Local AI DevOps Lab")


class PredictionRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(request: PredictionRequest):

    text = request.text.lower()

    positive_words = [
        "good",
        "great",
        "excellent",
        "fantastic",
        "amazing",
        "love"
    ]

    score = sum(word in text for word in positive_words)

    if score > 0:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"

    return {
        "text": request.text,
        "sentiment": sentiment
    }
