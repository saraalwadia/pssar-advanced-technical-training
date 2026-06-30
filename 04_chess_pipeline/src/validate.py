import pandas as pd
import logging

logger = logging.getLogger(__name__)


def validate_chess(df: pd.DataFrame) -> None:
    """
    Validate cleaned chess dataset.

    Checks:
    - Required columns exist
    - No null values in critical columns
    - Valid categorical values
    - Logical constraints
    - No duplicates
    """

    logger.info("Starting validation process...")

    # -----------------------------
    # 1. Required columns check
    # -----------------------------
    required_cols = [
        'rating_diff',
        'white_rating',
        'black_rating',
        'turns',
        'winner'
    ]

    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    logger.info("Required columns check passed")

    # -----------------------------
    # 2. Null check (important improvement)
    # -----------------------------
    null_cols = df[required_cols].isnull().sum()
    if null_cols.any():
        raise ValueError(f"Null values found:\n{null_cols}")

    logger.info("Null values check passed")

    # -----------------------------
    # 3. Winner validation
    # -----------------------------
    valid_winners = ['White', 'Black', 'Draw']

    invalid_mask = ~df['winner'].isin(valid_winners)
    if invalid_mask.any():
        invalid_values = df.loc[invalid_mask, 'winner'].unique()
        raise ValueError(f"Invalid winner values: {invalid_values}")

    logger.info("Winner values check passed")

    # -----------------------------
    # 4. Turns validation
    # -----------------------------
    if not pd.api.types.is_numeric_dtype(df['turns']):
        raise ValueError("Turns column must be numeric")

    if (df['turns'] < 1).any():
        raise ValueError("Turns must be >= 1")

    logger.info("Turns validation passed")

    # -----------------------------
    # 5. Duplicates check
    # -----------------------------
    dup_count = df.duplicated().sum()

    if dup_count > 0:
        raise ValueError(f"Found {dup_count} duplicate rows")

    logger.info("Duplicates check passed")

    # -----------------------------
    # Final success message
    # -----------------------------
    logger.info(f"Validation successful: {df.shape[0]} rows, {df.shape[1]} columns")