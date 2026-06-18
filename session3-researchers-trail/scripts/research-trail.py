import pandas as pd

df = pd.read_csv("../raw_data/researchers.csv")

# Filter
filtered = df[(df["is_active"] == True) & (df["h_index"] > 15)]

# Sort
filtered = filtered.sort_values("joined_year")

# Extract first letters of last names
letters = filtered["last_name"].str[0]

word = "".join(letters)

print("CP1 RESULT:", word) # CP1 RESULT: DATAOPENSDOORS