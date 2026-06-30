import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw_data", "chess_games.csv")

def load_chess_data():
    """
    Load chess dataset from raw folder.

    Returns:
        pd.DataFrame
    """
    df = pd.read_csv(DATA_PATH)
    return df


