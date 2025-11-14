# iDem Research Task (EN/FR)

Welcome! This mini-project is part of the selection process for a **Research
Assistant** role on the iDem project (“Inclusive Democratic Spaces for
Deliberation and Participation”).

You are given **two CSV datasets**, one for English and one for French, built
from wikipedia and vikidea texts with sentence-level annotations for
complexity classification.

We are interested in **how** you work:
- how you understand data  
- how you design and justify simple experiments  
- how clearly you explain your methods and findings  

There is no single “correct” answer.

---

## 1. Data

### Download data

The datasets used in this task can be downloaded from the GitHub Release:

https://github.com/Nouran-Khallaf/idem-candidate-task/releases/latest

Place both files into the `data/` folder before running the notebooks.

- `En-Dataset.csv` – English sentences  
- `Fr-Dataset.csv` – French sentences  

Each has the following columns:

- `ID` – document / article identifier
- `Name` – article title
- `Sentence` – a single sentence in that article (EN or FR)
- `Label` – binary label (1 = sentence annotated as **simplified**,  
  0 = sentence annotated as **complex**).  
- `LengthWords` – sentence length in tokens
- `LengthChars` – sentence length in characters

More detail is in `data/README.md`.

---

## 2. Tasks

Please work through the tasks below. Focus on **clarity of reasoning** and
**reproducibility**.

You may use either English, French, or both. When you choose only one language,
please say why.

### Task 0 – Quick data overview

Create a short overview of the datasets for each language:

1. Basic statistics:
   - number of sentences
   - distribution of `Label` (how many 0 / 1)
   - IQR range.
2. Inspect a small sample of sentences and comment briefly:
   - How would *you* describe the difference between “complex” and
     “simplified” sentences here?
   - Do you see obvious label noise or artefacts?

You can implement this in `src/01_data_overview.py` or a notebook.

---

### Task 1 – Estimate the *true* proportion of simplified sentences

The `Label` column gives an *imperfect* annotation of whether a sentence is
simplified (`Label = 1`) or complex (`Label = 0`).

We suspect that:

- some sentences labeled as **complex** are actually quite simple  
- some labeled as **simplified** are still quite complex

Your goal is to propose and justify an estimate of the **true proportion of
simplified sentences** in each dataset (EN/FR).

Please:

1. Start by computing the **naïve proportion**:  
   \#(Label = 1) / total.
2. Then design a method to obtain a **better estimate**, for example:
   - simple heuristic rules based on length or vocabulary
   - or a classifier trained on a subset that you consider “clean”
   - or another approach you can justify
3. Use your method to produce:
   - an adjusted estimate of the proportion of simplified sentences
   - for English and/or French
4. Explain:
   - what assumptions you made
   - what you think are the main sources of error
   - why your estimate might be more realistic than the naïve one

You can put your code in `src/02_estimate_simplified_proportion.py`.

We will compare your estimates against internal reference values, but we care
much more about **your methodology** than about matching our numbers.

---

### Task 2 – Build a small parallel (complex–simplified) corpus

Using the datasets, construct a small **sentence-level parallel corpus** of
likely `(complex_sentence, simplified_sentence)` pairs.

Hints / constraints:

- Sentences come from the same article (`ID`, `Name`).
- Articles may contain both complex and simplified sentences.
- There is no gold alignment at the sentence level; you must infer it.

Please:

1. Define a strategy for aligning sentences within each article, for example:
   - match each simplified sentence (`Label = 1`) to the closest complex
     sentence (`Label = 0`) in the same article according to some similarity
     measure (e.g. token overlap, cosine similarity in an embedding space, etc.)
2. Implement this pipeline for **French** (required) and optionally for English.
3. Apply quality filters (your choice), e.g.:
   - discard pairs with too low similarity
   - discard very short sentences
   - remove obvious duplicates
4. Save the final parallel corpus as e.g.:

   - `data/processed/fr_parallel.tsv`  
   - (optionally) `data/processed/en_parallel.tsv`

   with at least columns:
   - `article_id`, `article_name`, `complex`, `simple`, `similarity_score`

5. Report:
   - how many pairs your method produced
   - what filters you used
   - your impression of quality (supported by a few examples)

Place code in `src/03_build_parallel_corpus.py` or a notebook.

---

### Task 3 – Do something interesting with the corpora

Choose **one** of the following (or propose your own small idea):

1. **Complex vs simplified classifier**

   - Train a simple model (e.g. logistic regression, small transformer, etc.)
     to predict the `Label` from `Sentence` (EN or FR).
   - Evaluate on a held-out test set.
   - Include **at least a little error analysis**:
     - show some misclassified sentences and comment on patterns.

2. **Complexity scoring**

   - Define a numeric “complexity” score per sentence (e.g. based on length,
     lexical frequency, syntactic depth, LM perplexity, etc.).
   - Compare score distributions for Label 0 vs Label 1.
   - Discuss whether the scores match your intuition about complexity.

3. **Lexical simplification patterns**

   - Using your parallel corpus from Task 2, extract common word-level
     substitutions (complex → simple).
   - Provide some statistics and examples:
     - most frequent substitutions
     - types of words that tend to be simplified

Put code for this in `src/04_free_analysis.py` or a notebook.

---

## 3. Deliverables

Please include:

1. **Code / notebooks**

   - Place Python scripts in `src/` and any notebooks in `notebooks/`.
   - Code should be reasonably organised and runnable.

2. **Short slide presentation (preferred over a long report)**

   - Prepare a slide deck (up to **10 slides**), summarising:
     - problem understanding
     - methods
     - key results
     - main takeaways & limitations
   - Export slides as **PDF** and put in `reports/` (e.g. `reports/main_presentation.pdf`).

   A suggested slide outline is provided in `reports/presentation_outline.md`.

3. **Environment**

   - Include a `requirements.txt` (or `environment.yml`) listing your main
     dependencies.

---

## 4. Practical Notes

- You may use any standard Python / NLP libraries (NumPy, pandas, scikit-learn,
  spaCy, Hugging Face, etc.).
- Please keep computation reasonable for a typical laptop.
- We will look at:
  - how you deal with label noise and ambiguity
  - how you motivate design choices
  - whether the project is easy to run and understand

Thank you for your time — we look forward to your submission.
