def clean_attacks(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    df = df.dropna(how="all")
    return df