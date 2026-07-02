import pandas as pd
import sqlite3

# ─────────────────────────────
# CONNECT DB
# ─────────────────────────────
conn = sqlite3.connect("chess.db")

# ─────────────────────────────
# Q1 - Highest Draw Rate Opening
# ─────────────────────────────
q1 = """
SELECT 
    opening_code,
    COUNT(*) AS total_games,
    SUM(CASE WHEN winner = 'Draw' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS draw_rate
FROM games
GROUP BY opening_code
ORDER BY draw_rate DESC
LIMIT 1;
"""
print("Q1 - Highest Draw Rate Opening:", conn.execute(q1).fetchall())


# ─────────────────────────────
# Q2 - Black stronger players
# ─────────────────────────────
q2 = """
SELECT 
    black_id,
    SUM(CASE WHEN winner = 'Black' THEN 1 ELSE 0 END) AS black_wins,
    SUM(CASE WHEN winner = 'White' THEN 1 ELSE 0 END) AS white_wins
FROM games
GROUP BY black_id
HAVING black_wins > white_wins
ORDER BY (black_wins - white_wins) DESC
LIMIT 10;
"""
print("Q2 - Black stronger players:", conn.execute(q2).fetchall())


# ─────────────────────────────
# Q3 - Most common opening per victory_status
# ─────────────────────────────
q3 = """
SELECT 
    victory_status,
    opening_code,
    COUNT(*) AS cnt
FROM games
GROUP BY victory_status, opening_code
ORDER BY victory_status, cnt DESC;
"""
print("Q3 - Most common opening per victory_status:", conn.execute(q3).fetchall())


# ─────────────────────────────
# Q4 - Feature Table (JOIN + CTE)
# ─────────────────────────────
q4 = """
WITH base AS (
    SELECT 
        game_id,
        white_id,
        black_id,
        white_rating,
        black_rating,
        (white_rating - black_rating) AS rating_diff,
        turns,
        rated,
        opening_code,
        winner
    FROM games
),
white_exp AS (
    SELECT 
        white_id,
        COUNT(*) AS white_experience
    FROM games
    GROUP BY white_id
)

SELECT 
    b.game_id,
    b.rating_diff,
    b.turns,
    b.rated,
    b.opening_code AS opening_shortname,
    COALESCE(w.white_experience, 0) AS white_experience,
    b.winner
FROM base b
LEFT JOIN white_exp w
ON b.white_id = w.white_id;
"""

df_features = pd.read_sql_query(q4, conn)

df_features.to_csv("data/processed/features.csv", index=False)

print("Q4 - Feature table saved:", df_features.shape)

conn.close()