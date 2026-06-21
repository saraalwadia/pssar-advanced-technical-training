# Chess Database Project

## Overview
This project builds a relational SQLite database from chess game data and performs SQL analysis using SELECT, GROUP BY, JOINs, CTEs, Window Functions, and Index Optimization. It also includes feature engineering for further analysis or machine learning use.

---

## Database Schema

### games table
- game_id (TEXT, PRIMARY KEY)
- white_id (TEXT)
- black_id (TEXT)
- winner (TEXT: White / Black / Draw)
- turns (INTEGER)
- white_rating (INTEGER)
- black_rating (INTEGER)
- victory_status (TEXT)
- opening_code (TEXT)

Purpose: Stores all chess game records.

---

### players table
- username (TEXT, PRIMARY KEY)
- country (TEXT)

Purpose: Stores player information.

---

## Relationships
- games.white_id → players.username  
- games.black_id → players.username  

Foreign keys ensure data consistency between games and players.

---

## Indexing
Indexes were created on:
- games.white_id
- games.black_id
- games.opening_code

These indexes improve query performance for joins and filtering. EXPLAIN QUERY PLAN confirms index usage instead of full table scans.

---

## SQL Analysis
The project answers the following questions:
- Highest draw rate opening
- Players who perform better as Black than White
- Most common openings per victory status
- Game statistics using aggregation
- Player ranking using window functions

---

## Feature Engineering
A feature table was created containing:
- game_id
- rating_diff
- turns
- winner
- opening_shortname
- white_experience
- rated

Saved at:
data/processed/features.csv

---

## Window Functions
Used RANK and LAG functions to analyze:
- Player performance over time
- Game duration ranking per player
- Rating progression between games

---

## Data Cleaning
- Removed duplicates
- Standardized categorical values
- Ensured consistent schema before loading into database

---

## How to Run
python src/db.py
python src/assignment6.py
python src/joins_cte.py
python src/windows.py
python src/features.py

---

## Project Structure
chess_db/
├── src/
├── data/
│   ├── raw/
│   ├── processed/
├── chess.db
├── README.md

---

## Conclusion
This project demonstrates SQL database design, analytical querying, performance optimization using indexes, and feature engineering in a structured data pipeline.