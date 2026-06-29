# Data Pipeline Project — Shark Attacks & Chess Games

## Overview
This project builds a complete data pipeline using Python and Pandas.  
It includes data cleaning, transformation, validation, analysis, and visualization for two datasets:

- Shark Attacks Dataset (attacks.csv)
- Chess Games Dataset (chess_games.csv)

The goal is to apply real-world data engineering practices using a structured pipeline approach.

---

# 1. Shark Attacks Dataset

## Dataset Shape
- Original shape: (rows, columns) before cleaning  
- Cleaned shape: (after removing empty rows, duplicates, and metadata columns)

---

## Data Cleaning Decisions

### 1. Removed fully empty rows
- Rows with no data were dropped to ensure data quality.

### 2. Stripped column names
- Fixed trailing whitespace in column names.

### 3. Dropped metadata columns
- Removed columns like `href` and `pdf` because they are not useful for analysis.

### 4. Standardized "Fatal (Y/N)"
- Converted values to uppercase and removed inconsistencies.

### 5. Converted Age column
- Transformed Age into numeric format using `to_numeric`.

### 6. Cleaned Time column
- Standardized formatting by stripping whitespace.

### 7. Removed duplicates
- Ensured no repeated records exist.

---

## Missing Data Summary

- Age: contains missing values due to invalid or unknown entries
- Time: partially missing or inconsistent format

---

# 2. Chess Games Dataset

## Dataset Shape
- Original shape: (rows, columns)
- Cleaned shape: after processing and feature engineering

---

## Data Cleaning & Feature Engineering

### 1. Parsed time_increment
- Split into `time_base` and `time_inc`

### 2. Created rating_diff
- Difference between white and black ratings

### 3. Extracted opening_family
- Extracted main opening category from opening name

### 4. Removed high-null columns
- Dropped columns like `opening_response`

### 5. Flagged suspicious games
- Games with very low number of turns (< 5)

### 6. Removed duplicates
- Ensured dataset integrity

---

## Key Insights

- White win rate ≈ 50%
- Black win rate ≈ 45%
- Draws ≈ 5%

- Most common opening: Sicilian Defense
- Draw games have the longest average duration

---

# Visualizations

The following plots were generated:

### Shark Attacks
- Fatal (Y/N) distribution
- Age vs Year scatter plot
- Age distribution boxplot

### Chess Games
- Win counts by color
- Rating difference vs turns
- Turns distribution by victory status

All plots are saved in: output/plots/

---

# Pipeline Structure

The project follows a modular pipeline:

1. Load raw data
2. Clean data using reusable functions
3. Validate outputs
4. Save processed datasets
5. Generate visualizations

---

# Tools Used
- Python
- Pandas
- Matplotlib