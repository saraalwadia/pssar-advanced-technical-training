Chess Database Project — SQL Pipeline

Overview

This project builds a full SQL-based data pipeline using a chess games dataset (chess_games.csv) and a player registry (player_registry.csv).
The goal is to transform raw data into a structured relational database, perform SQL analysis, and generate ML-ready features.

The entire workflow is implemented using SQLite with Python.

Data Sources

The project uses two datasets:

chess_games.csv
Contains chess game information including:
game_id, white_id, black_id, winner, turns, white_rating, black_rating, victory_status, opening_code, moves

player_registry.csv
Contains player metadata:
username, country

Database Design

The SQLite database contains the following tables:

games
Stores chess game records:
game_id (Primary Key)
white_id
black_id
winner
turns
white_rating
black_rating
victory_status
opening_code

players
Stores player information:
username (Primary Key)
country

Foreign Key Logic (conceptual):
games.white_id → players.username
games.black_id → players.username

Data Quality Issues

Several issues were identified during exploration:

- No exact duplicate rows found
- 1,138 duplicate move sequences
- opening_response column is ~93.98% missing
- opening_variation column is ~28.22% missing
- 18 games have only 1 turn (suspicious / invalid games)

Data Cleaning Decisions

The following cleaning steps were applied:

- Dropped or ignored highly missing columns (opening_response)
- Extracted new features such as rating_diff = white_rating - black_rating
- Flagged suspicious games where turns < 5
- Ensured dataset integrity before analysis
- Confirmed no duplicate rows exist in final dataset

Indexing Strategy

Indexes were created to improve query performance:

- games.white_id
- games.black_id
- games.opening_code

Performance was verified using EXPLAIN QUERY PLAN.

Before indexing:
- Full table scan is used

After indexing:
- SQLite uses index lookup, improving query performance

Analytical SQL Results

Key findings from SQL analysis:

- Total games: 20,058
- Rated games: 16,155
- Victory status distribution:
  - Resign: most common
  - Mate
  - Out of Time
  - Draw

Win rates:
- White: 49.86%
- Black: 45.40%
- Draw: 4.74%

Most common openings:
- Sicilian Defense variations
- French Defense
- Queen’s Pawn Game

Feature Engineering

A machine learning feature table was created with one row per game.

Features include:

- rating_diff (white_rating - black_rating)
- turns (game length)
- opening_shortname (opening_code)
- white_experience (derived from rating threshold)
- winner encoded as label

This dataset is ready for classification models.

Window Functions

Advanced SQL window functions were used:

- RANK()
  Used to rank games per player based on rating

- LAG()
  Used to compare each game with the previous game for the same player

These allow sequential and player-level analysis without aggregating rows.

Conclusion

This project demonstrates a full data pipeline:

raw data → relational schema → SQL analysis → feature engineering → optimized queries

It focuses on:

- relational database design
- SQL analytical queries
- data cleaning and quality control
- ML-ready feature preparation
- performance optimization using indexes