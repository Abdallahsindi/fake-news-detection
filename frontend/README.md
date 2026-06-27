# Fake News Detection — Frontend

React + Vite + Tailwind CSS frontend for the Fake News Detection API.

## Local Development

```bash
cd frontend
npm install
npm run dev
```

Make sure the backend is running on `http://localhost:8000`.

## Production Deployment (Vercel)

1. Push the repo to GitHub.
2. On Vercel, create a **New Project** and connect your repo.
3. Set **Root Directory** to `frontend/`.
4. Add environment variable: `VITE_API_URL` = your backend URL.
5. Deploy.

## Environment Variables

| Variable        | Required | Default                | Description          |
|-----------------|----------|------------------------|----------------------|
| `VITE_API_URL`  | No       | `http://localhost:8000`| Backend API base URL |

## Build

```bash
npm run build
```
