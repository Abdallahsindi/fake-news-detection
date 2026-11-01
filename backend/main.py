import logging
import os
import sys
import traceback

import joblib
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import CORS_ORIGINS, PORT
from schemas import HealthResponse, PredictRequest, PredictResponse
from services import clean_text

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Fake News Detection API",
    description="Predict whether a news article is Fake News or Factual News using a Feedforward Neural Network (Keras/TensorFlow).",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "nn_model.keras")
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

model = None
vectorizer = None


@app.on_event("startup")
def startup():
    global model, vectorizer
    logger.info("Starting application...")
    for path, label in [(MODEL_PATH, "model"), (VECTORIZER_PATH, "vectorizer")]:
        if not os.path.exists(path):
            logger.error("%s file not found at %s", label, path)
            sys.exit(1)
        logger.info("Loading %s from %s...", label, path)
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        logger.info("nn_model.keras loaded successfully (input_shape=%s)", model.input_shape)
        vectorizer = joblib.load(VECTORIZER_PATH)
        logger.info("vectorizer.pkl loaded successfully (vocab_size=%d)", len(vectorizer.vocabulary_))
    except Exception as e:
        logger.error("Failed to load model artifacts: %s", e)
        logger.error(traceback.format_exc())
        sys.exit(1)
    logger.info("CORS origins: %s", CORS_ORIGINS)
    logger.info("Application startup complete")


@app.get("/", summary="Root")
def root():
    return {"message": "Fake News Detection API is running"}


@app.get("/health", response_model=HealthResponse, summary="Health check")
def health():
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return HealthResponse(status="healthy")


@app.post("/predict", response_model=PredictResponse, summary="Predict news authenticity")
def predict(request: PredictRequest):
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    raw = request.text.strip()
    logger.info("Incoming predict request (text_length=%d)", len(raw))

    if not raw:
        raise HTTPException(status_code=400, detail="Input text cannot be empty")

    try:
        cleaned = clean_text(raw)
        if not cleaned:
            raise HTTPException(status_code=400, detail="Input text is empty after cleaning")

        word_count = len(cleaned.split())
        if word_count < 15:
            raise HTTPException(
                status_code=400,
                detail=f"Text too short ({word_count} meaningful words found after cleaning). "
                       f"Please paste a full news article — minimum 15 words required for a reliable prediction."
            )

        # TF-IDF → dense array (Keras Dense layers require dense input)
        X = vectorizer.transform([cleaned]).toarray().astype(np.float32)
        prob = float(model.predict(X, verbose=0)[0][0])
        label = "Fake News" if prob >= 0.5 else "Factual News"
        confidence = round(prob if prob >= 0.5 else 1.0 - prob, 4)

        logger.info("Prediction: %s (prob=%.4f, confidence=%.4f, cleaned_length=%d)", label, prob, confidence, len(cleaned))
        return PredictResponse(prediction=label, confidence=confidence)

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Prediction failed: %s", e)
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal prediction error")


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting uvicorn on 0.0.0.0:%d", PORT)
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
