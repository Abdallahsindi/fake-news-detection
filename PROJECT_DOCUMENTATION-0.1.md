# Fake News Detection — Project Documentation

**Status:** Phase 1 (Data Cleaning) — ✅ Complete. Phase 2 (Model Training) — ⏳ Not started, ready to begin.
**Last updated:** June 27, 2026

---

## QUICK ANSWER (read this first if you're in a hurry)

**Q: Should we train the model now?**
**A: Yes — Phase 1 is fully done and verified. Training the model is the very next step (Phase 2).**
Nothing is blocking it. When you're back, just say "let's start Phase 2" / "train the model" and
work can begin immediately using `fake_news_data_clean.csv` as the input.

**Q: Was the cleaning done manually or automatically?**
**A: Automatically, by code.** Every cleaning step (missing-value checks, duplicate checks, date
fixing, text cleaning, etc.) is a line of Python/pandas code inside `01_Data_Cleaning.ipynb`. No
row was edited by hand. Running the notebook top-to-bottom redoes the entire cleaning automatically.

**Q: Does running the notebook automatically save the cleaned CSV?**
**A: Yes.** The last code cell in the notebook runs `df.to_csv('fake_news_data_clean.csv')`
automatically — no manual export step needed. That file already exists and is ready to use.

**Q: Have we covered Phase 2 in the course files provided?**
**A: Not fully.** Your course files cover the *modeling mechanics* we'll reuse (train/test split,
`.fit()`, `.predict()`, evaluation — from `02-Logistic_Regression_Project`), but none of your 20
course files cover **text vectorization** (turning words into numbers), since all your course
datasets were already numeric/categorical (Salaries, Ecommerce, Advertising). That one piece is
new and specific to this NLP project — everything else in Phase 2 will mirror what you've already
practiced.

---

## 1. Project Goal

Build an AI model that reads a news article (title + body text) and predicts whether it is
**Fake News** or **Factual News**. This is a binary text-classification problem.

The project is broken into phases:

| Phase | What | Status |
|---|---|---|
| **1** | Clean & prepare the raw dataset | ✅ Done (this doc covers it) |
| **2** | Vectorize text + train a classifier (e.g. Logistic Regression) | ⏳ Not started |
| **3** | Evaluate the model, tune it, maybe try other algorithms | ⏳ Not started |
| **4** | (Optional) Wrap it in something usable — script, simple app, etc. | ⏳ Not started |

---

## 2. Files in This Project

| File | Purpose |
|---|---|
| `fake_news_data.csv` | **Original raw data.** Never modify this — always treat it as the source of truth. |
| `01_Data_Cleaning.ipynb` | **Phase 1 notebook.** Loads the raw CSV, cleans it, saves the clean version. Fully commented. |
| `fake_news_data_clean.csv` | **Output of Phase 1.** This is what Phase 2 will load and build on. |
| `PROJECT_DOCUMENTATION.md` | This file. |

**If you come back to this later:** open `01_Data_Cleaning.ipynb` to see exactly how the data was
cleaned, and use `fake_news_data_clean.csv` as the starting point for Phase 2 — you don't need to
re-run the cleaning notebook unless you want to change something about the cleaning logic itself.

---

## 3. The Raw Dataset

- **198 rows, 4 columns:** `title`, `text`, `date`, `fake_or_factual`
- **Source:** uploaded CSV, appears to be a mix of mainstream news and fake/clickbait articles
  (titles range from neutral, e.g. *"Britain says window to restore Northern Ireland devolution
  closing rapidly"*, to clearly editorialized, e.g. *"HOLLYWEIRD LIB SUSAN SARANDON..."*).
- **Label balance:** 100 Factual News / 98 Fake News — close to 50/50, which is good. It means we
  won't need special techniques for class imbalance later, and plain accuracy will be a meaningful
  metric in Phase 2/3.

### Data quality issues found during inspection

1. **No missing values** (`isnull().sum()` was 0 across all columns) and **no duplicate rows**.
   Good news — but we still ran all the standard checks rather than assuming this.
2. **Inconsistent whitespace** — many `title` and `date` values had leading/trailing spaces
   (e.g. `" Elijah Cummings Called Trump..."`). Fixed with `.str.strip()`.
3. **Mixed date formats** — the `date` column has two different formats in the same column:
   - Full month names: `"September 18, 2017"`
   - Abbreviated month names: `"Dec 30, 2015"`
   Fixed using `pd.to_datetime(df['date'], format='mixed', errors='coerce')`, which lets pandas
   detect each row's format individually. Result: 0 unparseable dates.
4. **Smart/curly quotes** (`’ ‘ “ ”`) appear in several titles (e.g. `"Jesus' Family"` uses a curly
   apostrophe, not a straight one). Python's built-in `string.punctuation` doesn't include these
   Unicode characters, so they had to be added manually to the punctuation-stripping step —
   otherwise words like `"here's"` would incorrectly survive cleaning as `"here's"` instead of
   becoming `"heres"`.
5. **Missing apostrophes in the raw article text** — e.g. `"who s not paying attention"` instead
   of `"who's not paying attention"`. This looks like a scraping/export artifact in the original
   data, not something we caused. We deliberately did **not** try to guess and reinsert missing
   apostrophes, since that risks introducing new errors. It doesn't actually hurt the pipeline,
   since punctuation gets stripped during NLP cleaning anyway.

---

## 4. What the Cleaning Pipeline Does (Phase 1 Summary)

Step by step, in the order they appear in `01_Data_Cleaning.ipynb`:

1. **Load & inspect** — `pd.read_csv()`, then `.head()`, `.info()`, `.shape` to understand the data.
2. **Check missing data** — `.isnull().sum()` (and an extra check for empty strings, which
   `.isnull()` doesn't catch).
3. **Check duplicates** — `.duplicated()` on the full row and on `title`+`text` specifically.
4. **Strip whitespace** — `.str.strip()` on every text column.
5. **Encode the label** — map `"Fake News"` → `1`, `"Factual News"` → `0`, into a new `label` column.
   (Models need numbers, not text, as the target to predict.)
6. **Parse dates** — convert the `date` column from mixed-format strings into real `datetime`
   objects, then extract `year` and `month` as separate columns.
7. **Clean the text (NLP step)** — a custom `clean_text()` function applied to both `title` and
   `text`, producing `clean_title` and `clean_text`. This:
   - lowercases everything
   - removes URLs and email addresses
   - removes HTML tags
   - removes punctuation (including curly quotes)
   - removes standalone digits
   - collapses extra whitespace
   - removes English stopwords (`"the"`, `"and"`, `"is"`, etc.)
   - drops leftover single-character tokens
8. **Feature engineering** — a few cheap derived numeric columns that might be useful later:
   - `text_length` — character count of the raw article
   - `word_count` — word count of the cleaned article
   - `title_upper_ratio` — what fraction of the title's letters are uppercase (fake/clickbait
     headlines are sometimes ALL CAPS or partially capitalized for emphasis)
9. **Final review & save** — reorder columns logically, run final sanity checks, save to
   `fake_news_data_clean.csv`.

### Why no external NLP library (like NLTK)?

The sandbox this was built in has no internet access, so NLTK's stopword/corpora downloads aren't
available. Instead, the stopword list is defined directly in the notebook as a plain Python set.
This makes the notebook **fully self-contained** — it will run on any machine with just `pandas`
and `numpy` installed, no extra downloads required. If you later want to swap in NLTK or spaCy for
more sophisticated text processing (lemmatization, POS tagging, etc.), that's a reasonable Phase 2
upgrade, not something Phase 1 needs.

---

## 5. How This Connects to the Course Material

Per your request, the cleaning notebook deliberately mirrors techniques from your course notebooks
rather than introducing unfamiliar patterns:

| Technique | Used in cleaning notebook | Also appears in course file |
|---|---|---|
| `.head()`, `.info()`, `.describe()` | Section 1 | `Logistic_Regression_Project`, `DataFrames` |
| `.isnull().sum()`, missing-data handling | Section 2 | `Missing_Data` |
| `.duplicated()` | Section 3 | (standard DataFrame method, same family as `DataFrames`) |
| `.str.strip()` / string methods | Section 4 | `Python_Exercises_-_Solutions` (e.g. `s.split()`) |
| `.apply()` with a custom function | Sections 7–8 | `DataFrames`, `Groupby` |
| Writing custom `def` functions | Section 7 (`clean_text`), Section 8 (`uppercase_ratio`) | `Lab` (`welcome()`, `sum()`), `Python_Exercises_-_Solutions` (`domainGet()`, `findDog()`, `countDog()`, `caught_speeding()`) |
| `lambda` functions | Section 8 (`word_count` calc) | `Python_Exercises_-_Solutions` (`filter(lambda ...)`) |
| `pd.to_datetime()` | Section 6 | (standard pandas date handling) |
| `np.nan` / NumPy awareness | Section 2 discussion | `Numpy`, `Missing_Data` |
| `.to_csv()` | Section 10 | `Data_Input_and_Output` |

The **only genuinely new material** (not covered in the course) is the NLP-specific text cleaning
in Section 7 — lowercasing, punctuation/stopword removal — because none of the course's datasets
(salaries, ecommerce, advertising) involved free-form natural language text. That's a necessary
addition for this specific project, clearly marked in the notebook as **[NLP STEP]**.

---

## 6. Validation Performed

Before delivering, the entire notebook was extracted and executed end-to-end (not just visually
checked) to confirm it runs cleanly:

- ✅ 198 rows in → 198 rows out (no rows accidentally dropped)
- ✅ 0 missing values in any column, before or after cleaning
- ✅ 0 unparseable dates (down from an initial parsing issue, now fixed with `format='mixed'`)
- ✅ 0 duplicate rows
- ✅ 0 empty `clean_text` values after cleaning (cleaning didn't wipe any article down to nothing)
- ✅ Label balance preserved: 100 Factual / 98 Fake
- ✅ Output CSV (`fake_news_data_clean.csv`) loads back correctly with all 12 expected columns

---

## 7. Plan for Phase 2 (Next Steps)

When you're ready to continue, Phase 2 should:

1. **Load `fake_news_data_clean.csv`** (not the raw file).
2. **Split into train/test sets** — same `train_test_split` pattern from the Logistic Regression
   course project.
3. **Vectorize the text** — turn `clean_text` into numeric features the model can use. Common
   choices:
   - `CountVectorizer` (bag-of-words / word counts)
   - `TfidfVectorizer` (weights words by how distinctive they are — usually a better starting point)
4. **Train a baseline classifier** — Logistic Regression is the natural first choice since it's
   already covered in the course (`02-Logistic_Regression_Project`), and works well as a baseline
   for text classification.
5. **Evaluate** — accuracy, confusion matrix, precision/recall (since this is a binary
   classification problem, all of these are meaningful given the balanced classes).
6. **Iterate** — try other models (Naive Bayes is a classic baseline for text), tune
   hyperparameters, possibly bring in the `text_length`, `word_count`, and `title_upper_ratio`
   features alongside the vectorized text.

This documentation file should be enough to pick the project back up in a fresh conversation —
just re-upload `fake_news_data_clean.csv` (or re-run the Phase 1 notebook on the raw CSV) and
reference this file for context on what's already been decided and why.
