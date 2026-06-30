import pandas as pd
import os

# Define the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Build a safe, platform-independent path to the dataset
DATA_PATH = os.path.join(BASE_DIR, "data", "raw_data", "chess_games.csv")


def load_chess_data():
    """
    Load the raw chess dataset from the data directory.

    Returns:
        pd.DataFrame: Raw chess dataset loaded into memory
    """

    df = pd.read_csv(DATA_PATH)
    return df