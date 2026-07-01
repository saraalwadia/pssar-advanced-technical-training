import os
import pandas as pd

from src.clean_chess import clean_chess
from src.validate import validate_chess


RAW_DATA = "data/raw/chess_games.csv"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DIR, "chess_games_clean.csv")


def main():
    print("Loading dataset...")

    df = pd.read_csv(RAW_DATA)

    print(f"Loaded {len(df)} records.")

    print("Cleaning dataset...")
    df = clean_chess(df)

    print("Running validation...")
    validate_chess(df)

    os.makedirs(PROCESSED_DIR, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Clean dataset saved to: {OUTPUT_FILE}")
    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()