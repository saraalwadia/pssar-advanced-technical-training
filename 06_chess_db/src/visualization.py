import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# ─────────────────────────────
# Connect to database
# ─────────────────────────────
conn = sqlite3.connect("chess.db")

df = pd.read_sql("SELECT * FROM games", conn)

# ─────────────────────────────
# Create output folder
# ─────────────────────────────
os.makedirs("output/plots", exist_ok=True)

# ─────────────────────────────
# 1. BAR CHART — Wins by Color
# ─────────────────────────────
win_counts = df['winner'].value_counts()

plt.figure(figsize=(6,4))
win_counts.plot(
    kind='bar',
    color=['#2E3B4E', '#4C6A92', '#C9A84C']
)

plt.title("Wins by Color")
plt.xlabel("Winner")
plt.ylabel("Count")

plt.savefig("output/plots/wins_by_color.png", bbox_inches='tight')
plt.show()

# ─────────────────────────────
# 2. SCATTER — rating_diff vs turns
# ─────────────────────────────
df['rating_diff'] = df['white_rating'] - df['black_rating']

plt.figure(figsize=(6,4))

plt.scatter(
    df['rating_diff'],
    df['turns'],
    alpha=0.3,
    color='#4C6A92'
)

plt.title("Rating Difference vs Game Length")
plt.xlabel("Rating Difference")
plt.ylabel("Turns")

plt.savefig("output/plots/rating_vs_turns.png", bbox_inches='tight')
plt.show()

# ─────────────────────────────
# 3. BOXPLOT — turns by victory_status
# ─────────────────────────────
plt.figure(figsize=(7,5))

df.boxplot(
    column='turns',
    by='victory_status'
)

plt.title("Game Length by Victory Status")
plt.suptitle("")  # remove default pandas title
plt.xlabel("Victory Status")
plt.ylabel("Turns")

plt.savefig("output/plots/box_turns_by_victory_status.png", bbox_inches='tight')
plt.show()

# ─────────────────────────────
# Close connection
# ─────────────────────────────
conn.close()