import os
import logging

from src.load_data import load_chess_data
from src.clean_chess import clean_chess
from src.validate import validate_chess

# -----------------------------
# Create required folders
# -----------------------------
os.makedirs("logs", exist_ok=True)
os.makedirs("output", exist_ok=True)

# -----------------------------
# Logging setup (only once)
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# -----------------------------
# Pipeline function
# -----------------------------
def run_pipeline():
    logger.info("Pipeline started")

    # 1. Load
    df = load_chess_data()
    logger.info(f"Loaded data: {df.shape}")

    # 2. Clean
    df = clean_chess(df)
    logger.info(f"After cleaning: {df.shape}")

    # 3. Validate
    validate_chess(df)
    logger.info("Validation passed")

    # 4. Save
    output_path = os.path.join("output", "clean_chess.csv")
    df.to_csv(output_path, index=False)

    logger.info(f"Saved cleaned data to: {output_path}")

    logger.info("Pipeline finished successfully")

    return df


# -----------------------------
# Run pipeline
# -----------------------------
if __name__ == "__main__":
    run_pipeline()