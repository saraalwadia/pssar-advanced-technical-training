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
# 3. Create tables
# ─────────────────────────────
conn.execute("""
CREATE TABLE IF NOT EXISTS games (
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
CREATE TABLE IF NOT EXISTS players (
    username TEXT PRIMARY KEY,
    country TEXT
)
""")

# ─────────────────────────────
# 4. Load data into DB
# ─────────────────────────────
games.to_sql("games", conn, if_exists="replace", index=False)
players.to_sql("players", conn, if_exists="replace", index=False)

# ─────────────────────────────
# 5. Verify
# ─────────────────────────────
tables = conn.execute("""
SELECT name FROM sqlite_master WHERE type='table'
""").fetchall()

print("Tables in DB:", tables)

conn.close()