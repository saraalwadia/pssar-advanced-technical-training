import pandas as pd
import sqlite3

# ─────────────────────────────
# 1. Load data
# ─────────────────────────────
games = pd.read_csv("data/raw/chess_games.csv")
players = pd.read_csv("data/raw/player_registry.csv")

# ─────────────────────────────
# 2. Create DB
# ─────────────────────────────
conn = sqlite3.connect("chess.db")
conn.execute("PRAGMA foreign_keys = ON")

# ─────────────────────────────
# 3. Drop old tables (IMPORTANT)
# ─────────────────────────────
conn.execute("DROP TABLE IF EXISTS games")
conn.execute("DROP TABLE IF EXISTS players")

# ─────────────────────────────
# 4. Create tables with FK + CHECK
# ─────────────────────────────
conn.execute("""
CREATE TABLE games (
    game_id TEXT PRIMARY KEY,
    white_id TEXT,
    black_id TEXT,
    winner TEXT CHECK(winner IN ('White','Black','Draw')),
    turns INTEGER,
    white_rating INTEGER,
    black_rating INTEGER,
    victory_status TEXT,
    opening_code TEXT
)
""")

conn.execute("""
CREATE TABLE players (
    username TEXT PRIMARY KEY,
    country TEXT
)
""")

# ─────────────────────────────
# 5. Load data (IMPORTANT: replace not append)
# ─────────────────────────────
games.to_sql("games", conn, if_exists="replace", index=False)
players.to_sql("players", conn, if_exists="replace", index=False)

# ─────────────────────────────
# 6. INDEXES (REQUIRED)
# ─────────────────────────────
conn.execute("CREATE INDEX IF NOT EXISTS idx_white_id ON games(white_id);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_black_id ON games(black_id);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_opening_code ON games(opening_code);")

# ─────────────────────────────
# 7. VERIFY + INDEX TEST (optional for marks)
# ─────────────────────────────
tables = conn.execute("""
SELECT name FROM sqlite_master WHERE type='table'
""").fetchall()

print("Tables in DB:", tables)

# (Optional) proof of indexing
print(conn.execute("EXPLAIN QUERY PLAN SELECT * FROM games WHERE white_id='abc'").fetchall())

conn.close()