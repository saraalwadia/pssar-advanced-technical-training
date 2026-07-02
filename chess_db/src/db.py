import pandas as pd
import sqlite3

# ─────────────────────────────
# Load raw data
# ─────────────────────────────
games = pd.read_csv("data/raw/chess_games.csv")
players = pd.read_csv("data/raw/player_registry.csv")

# ─────────────────────────────
# CLEAN: keep only required columns (MOST IMPORTANT PART)
# ─────────────────────────────
games = games[[
    "game_id",
    "white_id",
    "black_id",
    "winner",
    "turns",
    "white_rating",
    "black_rating",
    "victory_status",
    "opening_code"
]]

players = players[[
    "username",
    "country"
]]

# ─────────────────────────────
# Create database connection
# ─────────────────────────────
conn = sqlite3.connect("chess.db")
conn.execute("PRAGMA foreign_keys = ON")

# ─────────────────────────────
# Reset tables
# ─────────────────────────────
conn.execute("DROP TABLE IF EXISTS games")
conn.execute("DROP TABLE IF EXISTS players")

# ─────────────────────────────
# Create tables (STRICT schema)
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
# Insert data into DB
# ─────────────────────────────
games.to_sql("games", conn, if_exists="append", index=False)
players.to_sql("players", conn, if_exists="append", index=False)

# ─────────────────────────────
# Indexes (REQUIRED FOR ASSIGNMENT)
# ─────────────────────────────
conn.execute("CREATE INDEX IF NOT EXISTS idx_white_id ON games(white_id);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_black_id ON games(black_id);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_opening_code ON games(opening_code);")

# ─────────────────────────────
# Verify
# ─────────────────────────────
print("Tables in DB:")
print(conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall())

print(conn.execute(
    "EXPLAIN QUERY PLAN SELECT * FROM games WHERE white_id='test'"
).fetchall())

conn.close()