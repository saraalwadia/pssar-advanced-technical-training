import pandas as pd
from src.clean_chess import clean_chess

def main():
    # 1. Load raw data
    df = pd.read_csv("data/raw/chess_games.csv")

    # 2. Clean data
    df = clean_chess(df)

    # 3. Simple validation
    assert df.duplicated().sum() == 0

    # 4. Save processed data
    df.to_csv("data/processed/chess_clean.csv", index=False)

    print("Pipeline executed successfully!")

if __name__ == "__main__":
    main()