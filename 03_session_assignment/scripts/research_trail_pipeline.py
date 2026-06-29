import pandas as pd
import os
import json

# BASE PATH
BASE = os.path.dirname(os.path.dirname(__file__))

# =============
# 1. LOAD DATA
# =============

# Researchers (CSV)
researchers_path = os.path.join(BASE, "raw_data", "researchers.csv")
researchers = pd.read_csv(researchers_path)

# Publications (JSON FIXED)
publications_path = os.path.join(BASE, "raw_data", "publications.json")

with open(publications_path, "r", encoding="utf-8") as f:
    publications = json.load(f)

pub_df = pd.json_normalize(publications)

# Funding (Excel)
funding_path = os.path.join(BASE, "raw_data", "funding.xlsx")
funding = pd.read_excel(funding_path)

print("Data Loaded Successfully")

# Inner join
inner_df = researchers.merge(pub_df, on="researcher_id", how="inner").merge(funding, on="researcher_id", how="inner")
print("Inner shape:", inner_df.shape) # Inner shape: (49, 23) | 49 rows

# Left join
left_df = researchers.merge(pub_df, on="researcher_id", how="left").merge(funding, on="researcher_id", how="left")
print("Left shape:", left_df.shape) # Left shape: (86, 23) | 86 rows

# Missed rows in inner join
print("Rows lost:", len(left_df) - len(inner_df)) # 37


# =========================
# 2. CLEAN FUNDING FUNCTION
# =========================

def clean_funding(df):
    df["amount_cad"] = pd.to_numeric(
        df["amount_cad"].astype(str).str.replace(",", ""),
        errors="coerce"
    )

    df = df[df["amount_cad"] > 0]
    return df

funding_clean = clean_funding(funding)

# =========================
# MERGE CLEANED DATASETS
# =========================

merged = pd.merge(
    researchers,
    pub_df,
    on="researcher_id",
    how="left"
)

final_df = pd.merge(
    merged,
    funding_clean,
    on="researcher_id",
    how="left"
)

print("\nFinal Shape:", final_df.shape)

# =========================
# 3. ANALYSIS
# =========================

# 1. Highest citations
citations = final_df.groupby("researcher_id")["citations"].sum()
top_researcher = citations.sort_values(ascending=False).head(1)

print("\nTop Researcher by Citations:")
print(top_researcher)
# researcher_id
# R001    20660.0
# Name: citations, dtype: float64

# 2. Field with most funding
field_funding = final_df.groupby("field")["amount_cad"].sum()
top_field = field_funding.sort_values(ascending=False).head(1)
print("\nTop Funded Field:")
print(top_field)
# field
# Data Engineering    960000.0
# Name: amount_cad, dtype: float64

# 3. Earliest active researcher
earliest = final_df[final_df["is_active"] == True]
earliest = earliest.sort_values("joined_year")

print("\nEarliest Active Researcher:")
print(earliest[["researcher_id", "joined_year"]].head(1))
# Earliest Active Researcher:
#    researcher_id  joined_year
# 53          R026         2006


# =========================
# 4. SAVE OUTPUT
# =========================

output_dir = os.path.join(BASE, "output")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "clean_research_data.csv")

final_df.to_csv(output_path, index=False)

print("\nSaved successfully at:")
print(output_path)