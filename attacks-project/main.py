from src.load import load_data
from src.clean import clean_attacks

df = load_data("data/raw/attacks.csv")
df = clean_attacks(df)

df.to_csv("data/processed/attacks_clean.csv", index=False)