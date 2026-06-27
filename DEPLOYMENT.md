# Deployment Guide

## Architecture

```
User Browser
     ↓
Vercel (React Frontend)
     ↓
Render/PythonAnywhere (FastAPI Backend)
     ↓
Random Forest Model → Prediction + Confidence
```

---

## 1. Backend — Deploy on Render

1. Push the repo to GitHub.
2. On Render, create a **New Web Service**.
3. Set **Root Directory** to `backend/`.
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy.

## 2. Backend — Deploy on PythonAnywhere

1. Upload the `backend/` folder to your PythonAnywhere account.
2. Create a new web app → Manual WSGI configuration.
3. Configure WSGI to point to `main:app`.
4. Open a PythonAnywhere console and run `pip install -r requirements.txt`.

## 3. Frontend — Deploy on Vercel

1. Push the repo to GitHub.
2. On Vercel, create a **New Project**.
3. Set **Root Directory** to `frontend/`.
4. Add environment variable: `VITE_API_URL` = your backend URL.
5. Deploy.

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.
