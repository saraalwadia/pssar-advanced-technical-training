import os
import logging

from src.load_data import load_chess_data
from src.clean_chess import clean_chess
from src.validate import validate_chess

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(level=logging.INFO)

# -----------------------------
# Pipeline function
# -----------------------------
def run_pipeline():
    logging.info("Pipeline started")

    # 1. Load
    df = load_chess_data()
    logging.info(f"Loaded data: {df.shape}")

    # 2. Clean
    df = clean_chess(df)
    logging.info(f"After cleaning: {df.shape}")

    # 3. Validate
    validate_chess(df)
    logging.info("Validation passed")

    # 4. Save
    output_path = os.path.join("output", "clean_chess.csv")
    df.to_csv(output_path, index=False)

    logging.info(f"Saved cleaned data to: {output_path}")

    logging.info("Pipeline finished successfully")

    return df


# -----------------------------
# Run pipeline
# -----------------------------
if __name__ == "__main__":
    run_pipeline()