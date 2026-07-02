import sqlite3

conn = sqlite3.connect("chess.db")

# ─────────────────────────────
# TEST QUERY
# ─────────────────────────────
query = "SELECT * FROM games WHERE white_id = 'taranga'"

query2 = "SELECT * FROM games WHERE black_id = 'taranga'"

# ─────────────────────────────
# BEFORE INDEX (or baseline plan)
# ─────────────────────────────
print("BEFORE INDEX (White):")
print(conn.execute("EXPLAIN QUERY PLAN " + query).fetchall())

print("BEFORE INDEX (Black):")
print(conn.execute("EXPLAIN QUERY PLAN " + query2).fetchall())

# ─────────────────────────────
# CREATE INDEXES (if not already created)
# ─────────────────────────────
conn.execute("CREATE INDEX IF NOT EXISTS idx_white_id ON games(white_id);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_black_id ON games(black_id);")

# ─────────────────────────────
# AFTER INDEX
# ─────────────────────────────
print("\nAFTER INDEX (White):")
print(conn.execute("EXPLAIN QUERY PLAN " + query).fetchall())

print("AFTER INDEX (Black):")
print(conn.execute("EXPLAIN QUERY PLAN " + query2).fetchall())

conn.close()