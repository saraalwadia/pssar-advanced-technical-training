# ♟️ Chess Database SQL Pipeline Challenge

## Project Overview
This project is a complete SQL-based data engineering pipeline built on a chess games dataset.  
The goal is to load raw CSV data into a SQLite database and perform structured analysis using SQL only (no Pandas for analysis).

The project is divided into 4 stages:
- Stage 0: Database setup
- Stage 1–2: SELECT & GROUP BY analysis
- Stage 3: JOINs & CTEs
- Stage 4: Window Functions

---

## Project Structure
chess_db/
│
├── data/
│ ├── raw/
│ │ ├── chess_games.csv
│ │ ├── player_registry.csv
│ │
│ ├── processed/
│
├── src/
│ ├── db.py
│ ├── queries.py
│ ├── joins_cte.py
│ ├── windows.py
│
├── chess.db
├── requirements.txt
├── README.md


---

## Database Schema

### Games Table
- game_id (TEXT, Primary Key)
- white_id (TEXT)
- black_id (TEXT)
- winner (TEXT: White / Black / Draw)
- turns (INTEGER)
- white_rating (INTEGER)
- black_rating (INTEGER)
- victory_status (TEXT)
- opening_code (TEXT)

### Players Table
- username (TEXT, Primary Key)
- country (TEXT)

---

### Key Results
Q1 — Total Games
20,058 games
Q2 — Victory Status Distribution
Resign: 11,147
Mate: 6,325
Out of Time: 1,680
Draw: 906
Q3 — Longest Games
Max turns: 349
Q4 — Win Rates
White: ~49.86%
Black: ~45.40%
Draw: ~4.74%
Q5 — Average Turns
Draw games are the longest (~83.8 turns)
Q6 — Most common openings
A00, C00, D00, B01, C41

### Advanced SQL Insights
JOIN Analysis
Top openings: A00, C00, D00
Player Analysis
~15 players never played as White
Win Leaders
Top players include: taranga, ssf7, hassan1365416

### Window Functions Insights
RANK() used to rank games per player by rating
LAG() used to compare consecutive games per player
Shows rating progression patterns per player

### Key Learnings
SQL aggregation techniques (GROUP BY, HAVING)
Data relationships using JOIN
Advanced SQL logic using CTEs
Time-series style analysis using Window Functions
Building full database pipeline from raw CSV

### Final Notes
This project demonstrates a full end-to-end SQL workflow:
Raw Data → Database → Analysis → Insights