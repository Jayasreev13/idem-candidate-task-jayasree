# Data description

This folder contains the sentence-level datasets for the lexical simplification
task.

## Files

- `En-Dataset.csv` – English sentences  
- `Fr-Dataset.csv` – French sentences  

Both files share the same schema:

| Column        | Type    | Description                                                  |
|---------------|---------|--------------------------------------------------------------|
| `ID`          | string  | Article / document identifier                                |
| `Name`        | string  | Article title                                                |
| `Sentence`    | string  | Individual sentence text (in EN or FR)                      |
| `Label`       | int     | 1 = sentence annotated as **simplified**, 0 = **complex**   |
| `LengthWords` | int     | Number of tokens in the sentence                            |
| `LengthChars` | int     | Number of characters in the sentence                        |

Notes:

- Articles are typically split into multiple sentences sharing the same `ID`
  and `Name`.
- The `Label` column is **noisy**: it is based on heuristic or crowd-sourced
  annotations. Some sentences may be mislabeled.
- `LengthWords` and `LengthChars` are provided to help you explore basic
  relationships between length and simplification.

You may create additional processed files (e.g. parallel corpora) under
`data/processed/`.

