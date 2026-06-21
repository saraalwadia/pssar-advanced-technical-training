import sqlite3

conn = sqlite3.connect("chess.db")
cur = conn.cursor()

# ─────────────────────────────
# Q1: Total games + rated games
# ─────────────────────────────
q1 = """
SELECT 
    COUNT(*) AS total_games,
    SUM(CASE WHEN white_rating IS NOT NULL THEN 1 ELSE 0 END) AS rated_games
FROM games;
"""
print("Q1:", cur.execute(q1).fetchall())

# ─────────────────────────────
# Q2: victory_status counts
# ─────────────────────────────
q2 = """
SELECT victory_status, COUNT(*) 
FROM games
GROUP BY victory_status;
"""
print("Q2:", cur.execute(q2).fetchall())

# ─────────────────────────────
# Q3: top 10 longest games
# ─────────────────────────────
q3 = """
SELECT game_id, winner, turns
FROM games
ORDER BY turns DESC
LIMIT 10;
"""
print("Q3:", cur.execute(q3).fetchall())

# ─────────────────────────────
# Q4: win rates
# ─────────────────────────────
q4 = """
SELECT 
    winner,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM games) AS win_rate
FROM games
GROUP BY winner;
"""
print("Q4:", cur.execute(q4).fetchall())

# ─────────────────────────────
# Q5: avg + max turns per status
# ─────────────────────────────
q5 = """
SELECT 
    victory_status,
    AVG(turns) AS avg_turns,
    MAX(turns) AS max_turns
FROM games
GROUP BY victory_status
ORDER BY avg_turns DESC;
"""
print("Q5:", cur.execute(q5).fetchall())

# ─────────────────────────────
# Q6: most common openings (>500)
# ─────────────────────────────
q6 = """
SELECT opening_code, COUNT(*) AS cnt
FROM games
GROUP BY opening_code
HAVING COUNT(*) > 500
ORDER BY cnt DESC;
"""
print("Q6:", cur.execute(q6).fetchall())

conn.close()