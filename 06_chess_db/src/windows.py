import sqlite3

conn = sqlite3.connect("chess.db")
cur = conn.cursor()

# ─────────────────────────────
# Q11: Rank games per player by rating
# ─────────────────────────────
q11 = """
SELECT 
    game_id,
    white_id,
    white_rating,
    RANK() OVER (
        PARTITION BY white_id 
        ORDER BY white_rating DESC
    ) AS rating_rank
FROM games
LIMIT 10;
"""
print("Q11:", cur.execute(q11).fetchall())

# ─────────────────────────────
# Q12: LAG - previous game rating per player
# ─────────────────────────────
q12 = """
SELECT 
    game_id,
    white_id,
    white_rating,
    LAG(white_rating) OVER (
        PARTITION BY white_id 
        ORDER BY game_id
    ) AS prev_rating
FROM games
WHERE white_id IN (
    SELECT white_id 
    FROM games 
    GROUP BY white_id 
    HAVING COUNT(*) >= 5
)
LIMIT 20;
"""
print("Q12:", cur.execute(q12).fetchall())

conn.close()