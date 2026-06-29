import pandas as pd
import json

# =========================
# 1. CSV FILE
# =========================
csv_path = "../raw_data/student_coffee_crisis.csv"
csv_df = pd.read_csv(csv_path)

print("\n===== CSV DATA =====")
print(csv_df.head())


# =========================
# 2. JSON FILE
# =========================
json_path = "../raw_data/student_coffee_crisis.json"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

json_df = pd.json_normalize(data)

print("\n===== JSON DATA =====")
print(json_df.head())


# =========================
# 3. EXCEL FILE
# =========================
excel_path = "../raw_data/student_coffee_crisis.xlsx"
excel_df = pd.read_excel(excel_path)

print("\n===== EXCEL DATA =====")
print(excel_df.head())


# =========================
# 4. PARQUET FILE
# =========================
parquet_path = "../raw_data/student_coffee_crisis.parquet"
parquet_df = pd.read_parquet(parquet_path)

print("\n===== PARQUET DATA =====")
print(parquet_df.head())