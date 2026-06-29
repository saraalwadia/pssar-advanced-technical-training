import pandas as pd

def clean_attacks(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean shark attacks dataset using 7-stage framework.
    Returns cleaned dataframe.
    """

    df = df.copy()  # never modify original

    # ─────────────────────────────
    # 1. Remove fully empty rows
    # ─────────────────────────────
    df = df.dropna(how="all")

    # ─────────────────────────────
    # 2. Strip column names
    # ─────────────────────────────
    df.columns = df.columns.str.strip()

    # ─────────────────────────────
    # 3. Drop metadata columns
    # ─────────────────────────────
    meta_cols = [c for c in df.columns if "href" in c.lower() or "pdf" in c.lower()]
    df = df.drop(columns=meta_cols, errors="ignore")

    # ─────────────────────────────
    # 4. Clean Fatal column (standardize values)
    # ─────────────────────────────
    if "Fatal (Y/N)" in df.columns:
        df["Fatal (Y/N)"] = (
            df["Fatal (Y/N)"]
            .astype(str)
            .str.strip()
            .str.upper()
        )

    # ─────────────────────────────
    # 5. Clean Age column (convert to numeric)
    # ─────────────────────────────
    if "Age" in df.columns:
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

    # ─────────────────────────────
    # 6. Clean Time column (keep as string, fix format)
    # ─────────────────────────────
    if "Time" in df.columns:
        df["Time"] = df["Time"].astype(str).str.strip()

    # ─────────────────────────────
    # 7. Remove duplicates
    # ─────────────────────────────
    df = df.drop_duplicates()

    # ─────────────────────────────
    # 8. Final validation
    # ─────────────────────────────
    assert df.duplicated().sum() == 0, "Duplicates still exist"

    return df