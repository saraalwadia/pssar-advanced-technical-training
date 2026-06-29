import pandas as pd
import os
from clean import clean_attacks
# Load raw data
df = pd.read_csv("data/raw/attacks.csv", encoding="latin1")

# Clean data
clean_df = clean_attacks(df)

# Save processed data
os.makedirs("data/processed", exist_ok=True)
clean_df.to_csv("data/processed/attacks_clean.csv", index=False)

print("✔ Pipeline completed successfully")