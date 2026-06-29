import pandas as pd
import json

df = pd.read_csv("../raw_data/researchers.csv")

# Filter
filtered = df[(df["is_active"] == True) & (df["h_index"] > 15)]

# Sort
filtered = filtered.sort_values("joined_year")

# Extract first letters of last names
letters = filtered["last_name"].str[0]

word = "".join(letters)

print("CP1 RESULT:", word) # CP1 RESULT: DATAOPENSDOORS

#############################################################

with open("../raw_data/publications.json", "r") as f:
    data = json.load(f)

df = pd.json_normalize(data)
print(df.head())

top_paper = df.sort_values("citations", ascending=False).iloc[0]

print("Top Paper Title:", top_paper["title"]) # Top Paper Title: Data Opens Doors: A Manifesto for Open Research
print("Researcher ID:", top_paper["researcher_id"]) # Researcher ID: R001

#############################################################

df = pd.read_excel("../raw_data/funding.xlsx")

print(df.head())
print(df.dtypes)

df["amount_cad"] = pd.to_numeric(
    df["amount_cad"].astype(str).str.replace(",", ""),
    errors="coerce"
)

clean_df = df[df["amount_cad"] > 0]
total_funding = clean_df["amount_cad"].sum()

print("TOTAL FUNDING:", total_funding) # TOTAL FUNDING: 2024000.0