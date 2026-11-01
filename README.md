# Fake News Detection

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=flat-square&logo=react&logoColor=black)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-8-646CFF?style=flat-square&logo=vite&logoColor=white)](https://vite.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

Classify a news article as **Fake News** or **Factual News** using classical machine
learning and deep learning, served through a FastAPI backend with a React front end.

The project covers the full pipeline: data cleaning, TF-IDF vectorisation, classical
baselines, a feedforward neural network, a text CNN, and a set of controlled experiments
(activation functions, optimisers, regularisation) that map to the course material.

## Results

Measured on the held-out test split of the bundled 199-article dataset:

| Model | Test accuracy | Macro F1 |
| --- | --- | --- |
| Feedforward NN (TF-IDF → Keras) — served by the API | 0.97 | — |
| 1D CNN over text embeddings | 0.95 | 0.95 |
| Experiment sweep (Perceptron, activations, optimisers) | — | 0.975 |

> **Note on the numbers.** The dataset is small (199 articles) and fairly separable, so
> these scores should be read as a pipeline demonstration, not as a claim about real-world
> performance. See `Project_Report_Abdullah_Sindi.pdf` for the full discussion and limitations.

## Repository layout

| Path | What it is |
| --- | --- |
| `01_Data_Cleaning.ipynb` | Loads the raw CSV, normalises text, removes duplicates, splits train/test |
| `02_Deep_Learning_Model.ipynb` | TF-IDF + Keras feedforward network (the deployed model) |
| `03_Experiments.ipynb` | Perceptron baseline, activation functions, optimisers, regularisation |
| `04_CNN_Text.ipynb` | 1D convolutional text classifier |
| `backend/` | FastAPI service that loads `nn_model.keras` + `vectorizer.pkl` and serves `/predict` |
| `frontend/` | React 19 + Vite + Tailwind UI for the live demo |
| `fake_news_data.csv` | Raw dataset (title, text, date, label) |
| `fake_news_data_clean.csv` | Cleaned dataset used by the notebooks |
| `Project_Report_Abdullah_Sindi.pdf` | Written report |
| `Neural_Networks_Project_QA.pdf` | Q&A prepared for the project defence |
| `Live_Demo_Test_QA.pdf` | Live demo script and test questions |

## Running locally

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API starts only if `nn_model.keras` and `vectorizer.pkl` are present next to `main.py`
(both are committed). Interactive docs: <http://localhost:8000/docs>.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Vite serves the UI on <http://localhost:5173> and proxies API calls to the backend on
port 8000. The allowed origins are configured through the `CORS_ORIGINS` environment
variable (see `backend/config.py`).

### Try the API

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Scientists announce a major breakthrough in cancer research."}'
```

```json
{
  "prediction": "Fake News",
  "confidence": 0.78
}
```

## API

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Root health check |
| `GET` | `/health` | Detailed health check |
| `POST` | `/predict` | Classify a news article |

More backend detail, including Render and PythonAnywhere deployment, is in
[`backend/README.md`](backend/README.md).

## Tech stack

| Layer | Tools |
| --- | --- |
| Data | pandas, NumPy, scikit-learn |
| Models | scikit-learn (TF-IDF, Perceptron, classical baselines), TensorFlow / Keras (FNN, 1D CNN) |
| Serving | FastAPI, Uvicorn, Pydantic |
| UI | React 19, Vite, Tailwind CSS 4, Axios |
| Deployment | Render / PythonAnywhere (backend), static hosting (frontend) |

## Limitations

- The dataset is small and balanced by construction; accuracy does not transfer directly to
  real news feeds.
- Text cleaning strips digits and punctuation, which removes useful signals such as dates
  and quotation marks.
- The model judges style and vocabulary, not factual correctness — a well-written false
  claim can still be classified as factual.

## License

Released under the [MIT License](LICENSE).
