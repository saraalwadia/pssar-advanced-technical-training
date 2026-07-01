import pandas as pd

# Load data
games_df = pd.read_csv("../data/raw/chess_games.csv")
players_df = pd.read_csv("../data/raw/player_registry.csv")

df = games_df.copy()

# Q1: How many records are in the dataset?
q1 = df.shape[0] # 20058
print("Q1 - Records:", q1)

# Q2: How many exact duplicate rows exist?
q2 = df.duplicated().sum() # 0
print("Q2 - Duplicate rows:", q2)

# Q3: How many games have duplicate move sequences?
q3 = df["moves"].duplicated().sum() # 1138
print("Q3 - Duplicate move sequences:", q3)

# Q4: What % of opening_response is missing?
q4 = df["opening_response"].isnull().mean() * 100 # 93.982450892412
print("Q4 - Missing % opening_response:", q4)

# Q5: What % of opening_variation is missing?
q5 = df["opening_variation"].isnull().mean() * 100 # 28.218167314787117
print("Q5 - Missing % opening_variation:", q5)

# Q6: What is the minimum number of turns in any game?
q6 = df["turns"].min() # 1
print("Q6 - Min turns:", q6)
