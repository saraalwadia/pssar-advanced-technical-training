import pandas as pd

def validate_chess(df: pd.DataFrame) -> None:
    """Validate cleaned chess dataset."""

    assert df.duplicated().sum() == 0, "Dataset contains duplicate rows."

    assert df["rating_diff"].notna().all(), "rating_diff contains missing values."

    assert df["turns"].min() >= 1, "Invalid number of turns."

    print("Validation passed.")