# Chess Data Pipeline

## Project Overview

This project was completed as part of the **PSSAR Advanced Technical Training** program.

The objective of this project is to build a complete data pipeline for a chess games dataset using Python and Pandas. The pipeline loads raw data, performs data cleaning and validation, engineers new features, analyzes the dataset, merges additional player information, and generates visualizations.

---

## Dataset

The project uses two datasets:

- `chess_games.csv`
- `player_registry.csv`

---

## Pipeline

The pipeline consists of the following stages:

1. Load raw datasets
2. Profile the data
3. Clean and transform the data
4. Validate the cleaned dataset
5. Save processed data
6. Analyze the data
7. Generate visualizations

---

## Data Cleaning

The cleaning pipeline performs the following operations:

- Parse the `time_increment` column into `time_base` and `time_inc`
- Create `rating_diff`
- Extract `opening_family`
- Remove the `opening_response` column due to excessive missing values
- Flag suspicious games with fewer than 5 turns

---

## Validation

The pipeline validates the cleaned dataset by checking:

- No duplicate rows
- No missing values in `rating_diff`
- Data integrity after feature engineering

---

## Analysis

The project answers several analytical questions, including:

- Win rate by color
- Most common game ending
- Average game length by victory status
- Opening popularity
- Rated vs unrated game comparison
- Game length classification

---

## Visualizations

The project generates and saves the following plots:

- Winner counts (Bar Chart)
- White rating vs. turns (Scatter Plot)
- Turns by victory status (Box Plot)

All plots are saved in:

```text
output/plots/
```

---

## Data Quality Report

### chess_games.csv

- Dataset contains **20,058** chess games.
- No exact duplicate rows were found.
- `opening_response` contains approximately **94%** missing values and was removed.
- `opening_variation` contains missing values but was retained because useful information is still available.
- Games with fewer than **5 turns** were flagged as suspicious.

### player_registry.csv

The registry dataset is used to enrich chess player information through merging. Missing registry records are expected because not every player appears in the registry.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

---

## How to Run

Create a virtual environment and install the required packages.

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python -m src.fetch_and_clean
```

---

## Author

Sara Alwadia

PSSAR Advanced Technical Training