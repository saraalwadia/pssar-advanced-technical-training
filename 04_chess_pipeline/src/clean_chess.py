import pandas as pd

def clean_chess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean chess dataset and create useful features.

    Steps:
    - Split time_increment into base + increment
    - Create rating_diff feature
    - Extract opening_family from opening_fullname
    - Drop noisy/unneeded columns

    Args:
        df (pd.DataFrame): Raw chess dataset

    Returns:
        pd.DataFrame: Cleaned dataset
    """

    # IMPORTANT: never modify original dataframe
    df = df.copy()

    # -------------------------------------------------
    # 1. Split time control safely
    # -------------------------------------------------
    time_split = df['time_increment'].fillna('0+0').str.split('+', expand=True)

    df['time_base'] = pd.to_numeric(time_split[0], errors='coerce')
    df['time_inc'] = pd.to_numeric(time_split[1], errors='coerce')

    # -------------------------------------------------
    # 2. Feature engineering
    # -------------------------------------------------
    df['rating_diff'] = df['white_rating'] - df['black_rating']

    # -------------------------------------------------
    # 3. Simplify opening name safely
    # -------------------------------------------------
    df['opening_family'] = (
        df['opening_fullname']
        .fillna('Unknown')
        .str.split(':').str[0].str.strip()
    )

    # -------------------------------------------------
    # 4. Drop noisy columns
    # -------------------------------------------------
    df = df.drop(columns=['opening_response'], errors='ignore')

    return df