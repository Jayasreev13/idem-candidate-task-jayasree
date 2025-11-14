import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def load_data():
    en = pd.read_csv(DATA_DIR / "En-Dataset.csv")
    fr = pd.read_csv(DATA_DIR / "Fr-Dataset.csv")
    return en, fr

def main():
    en, fr = load_data()
    # TODO: candidate implements stats & prints/plots

if __name__ == "__main__":
    main()
