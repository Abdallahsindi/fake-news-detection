# Fake News Detection — Project Documentation

## 1. Project Overview

This project builds a binary text-classification model that reads a news article (title and
body text) and predicts whether it is **Fake News** or **Factual News**.

### Status summary

| Phase | Description | Status |
|---|---|---|
| 1 | Clean and prepare the raw dataset | Complete |
| 2 | Vectorize text and train a classifier | Complete |
| 3 | Further evaluation, tuning, alternative models | Not started (optional) |
| 4 | Serve the model (e.g. via an API) | Not started |

**Phase 2 results:** TF-IDF + Logistic Regression — 95% test accuracy, ~94% mean 5-fold
cross-validation accuracy.

---

## 2. Project Files

| File | Description |
|---|---|
| `fake_news_data.csv` | Original raw dataset. Treated as read-only source of truth. |
| `01_Data_Cleaning.ipynb` | Phase 1 notebook — loads the raw CSV, cleans it, saves the cleaned version. |
| `fake_news_data_clean.csv` | Output of Phase 1; input to Phase 2. |
| `02_Model_Training.ipynb` | Phase 2 notebook — vectorizes text, trains and evaluates a classifier. |
| `PROJECT_DOCUMENTATION.md` | This file. |

To pick up the project: review `01_Data_Cleaning.ipynb` for the cleaning logic, then use
`fake_news_data_clean.csv` directly as the input to Phase 2 (no need to re-run Phase 1 unless
the cleaning logic itself needs to change).

---

## 3. Dataset

- **198 rows, 4 columns:** `title`, `text`, `date`, `fake_or_factual`
- **Label balance:** 100 Factual News / 98 Fake News — close to 50/50, so plain accuracy is a
  meaningful evaluation metric (no class-imbalance correction needed).

### Data quality issues identified and resolved in Phase 1

1. **No missing values, no duplicate rows** — confirmed via `isnull().sum()` and `.duplicated()`.
2. **Inconsistent whitespace** in `title`/`date` fields — resolved with `.str.strip()`.
3. **Mixed date formats** within the same column (e.g. `"September 18, 2017"` vs. `"Dec 30,
   2015"`) — resolved using `pd.to_datetime(df['date'], format='mixed', errors='coerce')`,
   resulting in 0 unparseable dates.
4. **Smart/curly quotes** (`’ ‘ “ ”`) in several titles, not covered by Python's standard
   `string.punctuation` — added manually to the punctuation-stripping step.
5. **Missing apostrophes in raw article text** (e.g. `"who s not paying attention"` instead of
   `"who's not paying attention"`), consistent with a scraping/export artifact in the source
   data. Not corrected via guesswork, since punctuation is stripped during NLP cleaning anyway
   and reinserting apostrophes would risk introducing errors.

---

## 4. Phase 1 — Data Cleaning Pipeline

Implemented in `01_Data_Cleaning.ipynb`:

1. **Load and inspect** — `pd.read_csv()`, `.head()`, `.info()`, `.shape`.
2. **Check missing data** — `.isnull().sum()`, plus a check for empty strings.
3. **Check duplicates** — `.duplicated()` on full rows and on `title` + `text` specifically.
4. **Strip whitespace** — `.str.strip()` on all text columns.
5. **Encode the label** — `"Fake News"` → `1`, `"Factual News"` → `0`, stored in a new `label`
   column.
6. **Parse dates** — mixed-format strings converted to `datetime` objects; `year`/`month`
   extracted.
7. **Clean text (NLP step)** — a custom `clean_text()` function applied to `title` and `text`,
   producing `clean_title` and `clean_text`: lowercasing, removal of URLs/emails/HTML
   tags/punctuation (including curly quotes)/digits, whitespace collapsing, stopword removal,
   and removal of single-character leftovers.
8. **Feature engineering** — adds `text_length` (raw character count), `word_count` (cleaned
   word count), and `title_upper_ratio` (fraction of uppercase letters in the title, a potential
   clickbait/fake-news signal).
9. **Final review and save** — column reordering, final sanity checks, output saved to
   `fake_news_data_clean.csv`.

**Note on dependencies:** the stopword list is defined directly as a Python set inside the
notebook rather than relying on an external library such as NLTK, keeping the notebook
self-contained with only `pandas` and `numpy` as dependencies.

### Validation performed (Phase 1)

The notebook was executed end-to-end and validated, not just visually reviewed:

- 198 rows in → 198 rows out (no rows dropped)
- 0 missing values, before and after cleaning
- 0 unparseable dates after applying `format='mixed'`
- 0 duplicate rows
- 0 empty `clean_text` values after cleaning
- Label balance preserved: 100 Factual / 98 Fake
- Output CSV loads back correctly with all 12 expected columns

---

## 5. Phase 2 — Model Training

Implemented in `02_Model_Training.ipynb`. Loads `fake_news_data_clean.csv` and:

1. Sets `X = clean_text`, `y = label`.
2. Splits into train/test sets (80/20) using `train_test_split(..., stratify=y)`. Stratification
   is used because the dataset is small (198 rows) and both sets need to preserve the ~50/50
   Fake/Factual balance.
3. **Vectorizes text with `TfidfVectorizer`** (max 5,000 features, `min_df=2`) — fit only on
   training data, then applied to test data, to avoid data leakage.
4. Trains a `LogisticRegression` model on the resulting TF-IDF features.
5. Evaluates the model with `classification_report`, a confusion matrix heatmap, and **5-fold
   cross-validation** — included because a single 198-row train/test split can be noisy, and CV
   gives a more reliable performance estimate.
6. Inspects the model's most influential words and reviews specific misclassified articles.
7. Provides a reusable `predict_article(raw_text)` function for testing the trained pipeline on
   arbitrary input text, returning a predicted label and confidence score.

### Results

- **Test accuracy: 95%** (38/40 correct on the held-out test set; 5% test error rate).
- **5-fold cross-validation:** scores of `[1.00, 0.925, 0.95, 0.82, 1.00]` — **mean accuracy ≈
  93.9%**, std ≈ 6.6%.
- **Confusion matrix:** 20/20 Factual News correctly identified; 18/20 Fake News correctly
  identified (2 misclassified as Factual).
- **Limitation:** with only 198 rows, cross-validation fold scores vary noticeably (82%–100%
  across folds), indicating results are somewhat sensitive to how the data happens to split. The
  ~94% mean CV accuracy is treated as the more reliable estimate than any single train/test
  split, and a larger dataset would make this estimate more stable.

### Model testing example

Using `predict_article()`, a neutral, real-sounding science headline ("Scientists at a major
university announced a new study...") was predicted as Fake News with only ~52% confidence —
effectively a coin flip. This reflects the dataset's small size (198 examples): low confidence
on unfamiliar-style text indicates the model correctly signaling uncertainty rather than
producing an unreliable result.

### Implementation note

Cross-validation in Section 5 step 5 uses separate `cv_tfidf` / `cv_model` objects rather than
the main `tfidf` / `logreg` objects used for training and prediction. Refitting the main
`tfidf` vectorizer on the full dataset for cross-validation would silently change its vocabulary
size, causing a feature-count mismatch when `predict_article()` later calls `tfidf.transform()`.
Keeping the two pairs of objects separate avoids this issue.

---

## 6. Handoff Notes for Model Deployment

The trained model is **not currently saved to a file**. `logreg` (the trained classifier) and
`tfidf` (the fitted vectorizer) exist only in memory while `02_Model_Training.ipynb` is running.

To use the trained model outside the notebook (e.g. in an API), either:

1. Re-run `02_Model_Training.ipynb` from top to bottom to recreate `logreg` and `tfidf` in
   memory, or
2. Persist both objects using `joblib.dump(logreg, ...)` and `joblib.dump(tfidf, ...)`, then load
   them with `joblib.load(...)` wherever the model is served.

**`tfidf` and `logreg` must be saved and loaded together as a pair.** The model was trained on
vectors produced by this specific `tfidf` vocabulary; new input text must be transformed using
the same vectorizer for predictions to be valid.

---

## 7. Possible Next Steps (Phase 3, Optional)

- Compare against an alternative model, e.g. `MultinomialNB` (Naive Bayes), a standard baseline
  for text classification.
- Combine TF-IDF text features with the numeric features from Phase 1 (`text_length`,
  `word_count`, `title_upper_ratio`) using `scipy.sparse.hstack`.
- Retrain on a larger dataset, if available, to assess whether cross-validation results become
  more stable.
- Use `GridSearchCV` to systematically tune `TfidfVectorizer` / `LogisticRegression`
  hyperparameters.
