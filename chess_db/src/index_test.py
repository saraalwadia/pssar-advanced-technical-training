import sqlite3

conn = sqlite3.connect("chess.db")

# Query before/after index
query = "SELECT * FROM games WHERE white_id = 'some_player'"

print(conn.execute("EXPLAIN QUERY PLAN " + query).fetchall())

query2 = "SELECT * FROM games WHERE black_id = 'some_player'"
print(conn.execute("EXPLAIN QUERY PLAN " + query2).fetchall())

conn.close()