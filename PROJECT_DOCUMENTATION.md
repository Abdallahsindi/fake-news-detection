# Fake News Detection — Project Documentation

**Last updated:** June 27, 2026
**Purpose of this file:** A complete, standalone snapshot of this project. If you open a brand
new chat with zero memory of this conversation, paste/upload this file first — it has everything
needed to pick up exactly where things left off.

---

## 0. ONE-LINE STATUS

✅ Phase 1 (Data Cleaning) — Done, verified, pushed to GitHub.
⏳ Phase 2 (Model Training) — Not started yet. This is the very next step, no blockers.
✅ GitHub repo — Created, private, Phase 1 files pushed successfully.
⏳ Teammates — Invited, not yet accepted/active as of this writing.

---

## 1. Project Goal

Build an AI model that reads a news article (title + body text) and predicts whether it is
**Fake News** or **Factual News**. This is a binary text-classification problem, built as a
group project (3 people) for a course, to be submitted/shown via a GitHub repository.

### Phase breakdown

| Phase | What | Status |
|---|---|---|
| **1** | Clean & prepare the raw dataset | ✅ Done |
| **2** | Vectorize text + train a classifier (e.g. Logistic Regression) | ⏳ Not started — next step |
| **3** | Evaluate the model, tune it, maybe try other algorithms | ⏳ Not started |
| **4** | (Optional) Wrap it in something usable — script, simple app, etc. | ⏳ Not started |

---

## 2. Files in the Project

| File | Purpose | Status |
|---|---|---|
| `fake_news_data.csv` | **Original raw data.** Never modify — always treat as source of truth. | ✅ On GitHub |
| `01_Data_Cleaning.ipynb` | **Phase 1 notebook.** Loads raw CSV, cleans it, saves clean version. Fully commented. | ✅ On GitHub |
| `fake_news_data_clean.csv` | **Output of Phase 1.** Starting point for Phase 2. | ✅ On GitHub |
| `PROJECT_DOCUMENTATION.md` | This file. | ✅ On GitHub (keep updating it each session) |
| *(Phase 2 notebook — not yet created)* | Will vectorize text + train + evaluate a classifier | ⏳ To be built |

**If picking this up cold:** open `01_Data_Cleaning.ipynb` to see exactly how the data was cleaned.
Use `fake_news_data_clean.csv` as the input for Phase 2 — no need to re-run Phase 1 unless you
want to change the cleaning logic itself.

---

## 3. The Raw Dataset — What We Found

- **198 rows, 4 columns:** `title`, `text`, `date`, `fake_or_factual`
- **Label balance:** 100 Factual News / 98 Fake News — close to 50/50 (good — no class imbalance
  problem to deal with later; plain accuracy will be a meaningful metric in Phase 2/3).

### Data quality issues found and fixed during Phase 1

1. **No missing values, no duplicate rows** — confirmed via `isnull().sum()` and `.duplicated()`,
   not assumed.
2. **Inconsistent whitespace** — many `title`/`date` values had leading/trailing spaces. Fixed
   with `.str.strip()`.
3. **Mixed date formats in the same column** — some rows used full month names
   (`"September 18, 2017"`), others abbreviated (`"Dec 30, 2015"`). Fixed using
   `pd.to_datetime(df['date'], format='mixed', errors='coerce')`. Result: 0 unparseable dates.
4. **Smart/curly quotes** (`’ ‘ “ ”`) in several titles — not covered by Python's standard
   `string.punctuation`, so they were added manually to the punctuation-stripping step.
5. **Missing apostrophes in raw article text** (e.g. `"who s not paying attention"` instead of
   `"who's not paying attention"`) — looks like a scraping/export artifact in the original data.
   Deliberately **not** "fixed" by guessing reinsertions (too risky for accuracy); doesn't hurt the
   pipeline since punctuation gets stripped during NLP cleaning anyway.

---

## 4. What the Phase 1 Cleaning Pipeline Does

Step by step, as implemented in `01_Data_Cleaning.ipynb`:

1. **Load & inspect** — `pd.read_csv()`, then `.head()`, `.info()`, `.shape`.
2. **Check missing data** — `.isnull().sum()` + an extra check for empty strings.
3. **Check duplicates** — `.duplicated()` on full rows and on `title`+`text` specifically.
4. **Strip whitespace** — `.str.strip()` on every text column.
5. **Encode the label** — `"Fake News"` → `1`, `"Factual News"` → `0`, into a new `label` column.
6. **Parse dates** — mixed-format strings → real `datetime` objects, then extract `year`/`month`.
7. **Clean the text (NLP step)** — custom `clean_text()` function applied to `title` and `text`,
   producing `clean_title` and `clean_text`. Lowercases, removes URLs/emails/HTML tags/punctuation
   (including curly quotes)/digits, collapses whitespace, removes English stopwords, drops
   single-character leftovers.
8. **Feature engineering** — adds `text_length` (raw character count), `word_count` (cleaned word
   count), `title_upper_ratio` (fraction of title letters that are uppercase — a possible
   clickbait/fake-news signal).
9. **Final review & save** — reorders columns, runs final sanity checks, saves to
   `fake_news_data_clean.csv`.

### Why no external NLP library (e.g. NLTK)?

The environment this was built in has no internet access for downloading NLTK's corpora, so the
stopword list is defined directly as a plain Python set inside the notebook. This makes the
notebook **fully self-contained** — runs anywhere with just `pandas` + `numpy`, no extra downloads.
A reasonable Phase 2/3 upgrade later would be swapping in NLTK/spaCy for lemmatization if you want
to go further, but it's not required.

---

## 5. How This Maps to the Course Material

| Technique used | Course file it came from |
|---|---|
| `.head()`, `.info()`, `.describe()` | `02-Logistic_Regression_Project`, `03-DataFrames` |
| `.isnull().sum()`, missing-data handling | `04-Missing_Data` |
| `.duplicated()` | Standard DataFrame method, same family as `03-DataFrames` |
| `.str.strip()` / string methods | `Python_Exercises_-_Solutions` (e.g. `s.split()`) |
| `.apply()` with a custom function | `03-DataFrames`, `05-Groupby` |
| Writing custom `def` functions | `Lab` (`welcome()`, `sum()`), `Python_Exercises_-_Solutions` (`domainGet()`, `findDog()`, `countDog()`, `caught_speeding()`) |
| `lambda` functions | `Python_Exercises_-_Solutions` (`filter(lambda ...)`) |
| `pd.to_datetime()` | Standard pandas date handling |
| `np.nan` / NumPy awareness | `Numpy`, `04-Missing_Data` |
| `.to_csv()` | `08-Data_Input_and_Output` |

**The only genuinely new material** beyond the course is the NLP text-cleaning in Section 7
(lowercasing, punctuation/stopword removal) — none of the course's datasets (salaries, ecommerce,
advertising) involved free-form natural language text, so this addition was necessary.

---

## 6. Validation Already Performed (Phase 1)

The entire notebook was extracted and executed end-to-end (not just visually checked):

- ✅ 198 rows in → 198 rows out (no rows accidentally dropped)
- ✅ 0 missing values, before or after cleaning
- ✅ 0 unparseable dates (after fixing with `format='mixed'`)
- ✅ 0 duplicate rows
- ✅ 0 empty `clean_text` values after cleaning
- ✅ Label balance preserved: 100 Factual / 98 Fake
- ✅ Output CSV loads back correctly with all 12 expected columns

---

## 7. GitHub Setup — Full Status

### What's done

- **Git installed** on Windows (version 2.54.0), identity configured (`user.name`, `user.email`
  both verified set).
- **Private repository created** on GitHub (visible only to invited collaborators).
- **Local project folder:** `C:\Users\alye0\OneDrive\Desktop\AMIT\Project`
  (Note: this folder is under OneDrive due to a Windows default that syncs Desktop automatically —
  this is harmless for Git, just something to be aware of if odd file-lock errors ever appear;
  retry the command if so.)
- **Repo initialized and connected** (`git init`, `git remote add origin ...`, `git branch -M main`).
- **Pulled GitHub's initial README** with `git pull origin main --allow-unrelated-histories`
  (needed because the repo was created with "Add a README file" checked).
- **Phase 1 files committed and pushed successfully:**
  - `fake_news_data.csv`
  - `fake_news_data_clean.csv`
  - `01_Data_Cleaning.ipynb`
  - `PROJECT_DOCUMENTATION.md`
  - Confirmed via `git push -u origin main` actually transferring objects (not "Everything
    up-to-date" — a real push happened).

### What's NOT done yet

- **Teammates invited via Settings → Collaborators, but not yet accepted/active.** Once you have
  their GitHub usernames, list them here:
  - Teammate 1 GitHub username: `___________`
  - Teammate 2 GitHub username: `___________`
- Once they accept the invite, each of them needs to run (one time):
  ```bash
  git clone https://github.com/yourusername/fake-news-detection.git
  ```
  And afterward, whenever someone pushes new work, the others just run:
  ```bash
  git pull
  ```
  to get the latest files.
- **No `README.md` (repo front page) or `.gitignore` set up yet** — optional polish, not urgent.
  A `.gitignore` would prevent junk files (like Jupyter checkpoint folders) from accidentally
  getting committed later.

### Day-to-day workflow going forward (for all 3 of you)

1. Pull first, to make sure you have the latest: `git pull`
2. Do your work (edit/add files)
3. Stage your changes: `git add .`
4. Commit with a clear message: `git commit -m "describe what you did"`
5. Push: `git push`

If two people edit the *same* file at the *same* time before pushing, Git may report a "merge
conflict" — this hasn't happened yet, but if it does in a future session, that's a normal Git
situation with a standard fix; just flag it and ask for help resolving it rather than worrying.

---

## 8. Plan for Phase 2 (Next Step — Not Started Yet)

This is the very next thing to do, whenever you're back. Plan:

1. **Load `fake_news_data_clean.csv`** (not the raw file) into a new notebook
   (e.g. `02_Model_Training.ipynb`).
2. **Split into train/test sets** — same `train_test_split` pattern from the course's
   `02-Logistic_Regression_Project`.
3. **Vectorize the text** — turn `clean_text` into numeric features the model can use:
   - `CountVectorizer` (bag-of-words / word counts), or
   - `TfidfVectorizer` (weights words by how distinctive they are — usually the better starting
     point for this kind of task)
4. **Train a baseline classifier** — Logistic Regression, since it's already covered in the
   course and is a strong, simple baseline for text classification.
5. **Evaluate** — accuracy, confusion matrix, precision/recall (meaningful here since classes
   are balanced).
6. **Iterate** — try other models (Naive Bayes is a classic text-classification baseline), tune
   hyperparameters, possibly combine the vectorized text with the extra numeric features already
   built in Phase 1 (`text_length`, `word_count`, `title_upper_ratio`).

### Important reminder for whoever does Phase 2

None of the course files cover text vectorization — that's the one genuinely new technique needed
here, since all the course datasets (Salaries, Ecommerce, Advertising) were already numeric. The
rest of Phase 2 (train/test split, `.fit()`, `.predict()`, evaluation metrics) directly reuses what
was practiced in `02-Logistic_Regression_Project`.

---

## 9. How to Resume in a Fresh Conversation

If starting a new chat with no memory of this one:

1. Upload this `PROJECT_DOCUMENTATION.md` file first.
2. Upload `fake_news_data_clean.csv` (and `01_Data_Cleaning.ipynb` if relevant).
3. Say something like: "Continue this project — start Phase 2: vectorize the text and train a
   Logistic Regression model, following the plan in section 8 of the attached documentation."
4. Fill in the teammate GitHub usernames in Section 7 once you have them, so the new chat can help
   with any further Git/GitHub steps (like resolving a merge conflict, or writing the README/`.gitignore`).

**Remember to ask for this documentation file to be updated again at the end of every future
session**, so it stays an accurate, current snapshot of the whole project.
