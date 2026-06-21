import sqlite3
import pandas as pd

# ─────────────────────────────
# Connect to DB
# ─────────────────────────────
conn = sqlite3.connect("chess.db")

# ─────────────────────────────
# Feature Engineering SQL
# ─────────────────────────────
query = """
SELECT
    game_id,
    (white_rating - black_rating) AS rating_diff,
    turns,
    CASE WHEN winner IS NULL THEN 'Unknown' ELSE winner END AS winner,

    CASE
        WHEN opening_code IS NULL THEN 'Unknown'
        ELSE opening_code
    END AS opening_shortname,

    CASE
        WHEN white_rating > 2000 THEN 1
        ELSE 0
    END AS white_experience,

    CASE
        WHEN winner = 'White' THEN 1
        WHEN winner = 'Black' THEN 0
        ELSE 0.5
    END AS rated

FROM games;
"""

# ─────────────────────────────
# Load into DataFrame
# ─────────────────────────────
df_features = pd.read_sql(query, conn)

# ─────────────────────────────
# Save CSV
# ─────────────────────────────
df_features.to_csv("data/processed/features.csv", index=False)

print("Features file created successfully!")

conn.close()