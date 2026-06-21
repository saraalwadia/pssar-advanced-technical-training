import sqlite3

conn = sqlite3.connect("chess.db")
cur = conn.cursor()

# ─────────────────────────────
# Q7: JOIN games + openings (top 5 openings)
# ─────────────────────────────
q7 = """
SELECT opening_code, COUNT(*) AS cnt
FROM games
GROUP BY opening_code
ORDER BY cnt DESC
LIMIT 5;
"""
print("Q7:", cur.execute(q7).fetchall())

# ─────────────────────────────
# Q8: players who never played as white
# ─────────────────────────────
q8 = """
SELECT p.username
FROM players p
LEFT JOIN games g ON p.username = g.white_id
WHERE g.white_id IS NULL;
"""
print("Q8 count:", len(cur.execute(q8).fetchall()))

# ─────────────────────────────
# Q9: top 5 players by white wins (CTE)
# ─────────────────────────────
q9 = """
WITH white_wins AS (
    SELECT white_id AS player, COUNT(*) AS wins
    FROM games
    WHERE winner = 'White'
    GROUP BY white_id
)
SELECT player, wins
FROM white_wins
ORDER BY wins DESC
LIMIT 5;
"""
print("Q9:", cur.execute(q9).fetchall())

# ─────────────────────────────
# Q10: total wins (white + black) using UNION
# ─────────────────────────────
q10 = """
WITH all_wins AS (
    SELECT white_id AS player FROM games WHERE winner = 'White'
    UNION ALL
    SELECT black_id AS player FROM games WHERE winner = 'Black'
)
SELECT player, COUNT(*) AS total_wins
FROM all_wins
GROUP BY player
ORDER BY total_wins DESC
LIMIT 5;
"""
print("Q10:", cur.execute(q10).fetchall())

conn.close()