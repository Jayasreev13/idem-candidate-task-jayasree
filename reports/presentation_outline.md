# iDem Research Task – 5‑Slide Presentation


---

## **Slide 1 — Data Understanding (EN & FR)**

* Two datasets (EN/FR) combining Wikipedia + Vikidia sentences.
* Columns: `Sentence`, `Label` (0 = simple, 1 = complex), length features.
* Observations: Vikidia is shorter/simpler; Wikipedia varies more. Some label noise + near-duplicate Wiki/Vikidia sentences.

---

## **Slide 2 — Task 0: Quick Overview**

* Stats: sentence counts, label distribution, length IQR (words/chars).
* Notes: mild imbalance; some long "simple" sentences; some "complex" ones appear simple.
* Early signs of noise and style overlap.

---

## **Slide 3 — Task 1: Estimating True Simple Proportion**


**Improved estimation:**

* Detect mislabeled simple sentences inside the "complex" group using:

  * similarity to Vikidia, **or**
  * a classifier trained on clean subsets.

**Output:**
* estimated % of Vikidia-like sentences inside Wiki

---

## **Slide 4 — Task 2: Additional Analysis**

(Example: simple vs complex classifier)
* Report accuracy/F1.
* Error examples: short but dense sentences → predicted complex; long/simple → predicted simple.

---

## **Slide 5 — Takeaways **

**Learnings:** 
**Limitations:** 
