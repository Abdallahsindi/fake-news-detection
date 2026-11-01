# Fake News Detection API

FastAPI backend that serves predictions from a trained Random Forest classifier with TF-IDF vectorization.

## Local Development

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Production Deployment (PythonAnywhere / Render)

### PythonAnywhere

1. Upload the `backend/` folder to your PythonAnywhere account.
2. Create a web app with manual WSGI configuration pointing to `main:app`.
3. Install dependencies via the PythonAnywhere console: `pip install -r requirements.txt`.

### Render

1. Push the repo to GitHub.
2. On Render, create a **New Web Service** and connect your repo.
3. Set **Root Directory** to `backend/`.
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Endpoints

| Method | Path       | Description               |
|--------|------------|---------------------------|
| GET    | `/`        | Root health check         |
| GET    | `/health`  | Detailed health check     |
| POST   | `/predict` | Predict news authenticity |

## Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Scientists announce a major breakthrough in cancer research."}'
```

### Response

```json
{
  "prediction": "Fake News",
  "confidence": 0.78
}
```

## Environment Variables

| Variable        | Required | Default | Description                       |
|-----------------|----------|---------|-----------------------------------|
| `CORS_ORIGINS`  | No       | `*`     | Comma-separated allowed origins   |
| `PORT`          | No       | `8000`  | Server port                       |

## Swagger Docs

Open `http://localhost:8000/docs` in your browser.

## Architecture

```
User Input → Text Cleaning → TF-IDF Vectorizer → Random Forest → Prediction + Confidence
```
