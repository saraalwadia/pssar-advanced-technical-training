import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)


def validate_chess(df: pd.DataFrame) -> None:
    """
    Validate cleaned chess dataset.

    This function checks:
    - Required columns exist
    - No invalid values
    - No duplicates
    - Logical constraints are satisfied

    Args:
        df (pd.DataFrame): Cleaned chess dataset

    Returns:
        None (raises error if validation fails)
    """

    logging.info("Starting validation...")

    # -----------------------------
    # 1. Check required columns
    # -----------------------------
    required_cols = [
        'rating_diff',
        'white_rating',
        'black_rating',
        'turns',
        'winner'
    ]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    logging.info("Required columns exist")

    # -----------------------------
    # 2. Validate winner values
    # -----------------------------
    valid_winners = ['White', 'Black', 'Draw']

    if not df['winner'].isin(valid_winners).all():
        invalid_values = df[~df['winner'].isin(valid_winners)]['winner'].unique()
        raise ValueError(f"Invalid winner values found: {invalid_values}")

    logging.info("Winner values are valid")

    # -----------------------------
    # 3. Validate turns
    # -----------------------------
    if (df['turns'] < 1).any():
        raise ValueError("Invalid turns detected (must be >= 1)")

    logging.info("Turns are valid")

    # -----------------------------
    # 4. Check duplicates
    # -----------------------------
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        raise ValueError(f"Found {duplicates} duplicate rows")

    logging.info("No duplicates found")

    # -----------------------------
    # 5. Check nulls in critical columns
    # -----------------------------
    critical_cols = ['white_rating', 'black_rating', 'turns', 'winner']

    null_counts = df[critical_cols].isnull().sum()

    if null_counts.any():
        raise ValueError(f"Null values found in critical columns:\n{null_counts}")

    logging.info("No nulls in critical columns")

    # -----------------------------
    # 6. Final success message
    # -----------------------------
    logging.info(f"Validation passed: {df.shape[0]} rows, {df.shape[1]} columns")