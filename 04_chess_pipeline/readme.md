Chess Data Cleaning Pipeline

Overview

This project is a simple data engineering pipeline that loads, cleans, validates, and saves a chess games dataset.

The main goal is to practice building a structured and reusable pipeline using Python and Pandas.

Pipeline Steps

1. Load raw chess dataset from CSV file
2. Clean the data and create new features
3. Validate data quality and logical consistency
4. Save the cleaned dataset to an output file

How to Run the Project

Install dependencies:

pip install pandas

Run the pipeline:

python -m src.pipeline

Data Cleaning Steps

- Split time_increment into time_base and time_inc
- Create rating_diff feature (difference between white and black ratings)
- Extract opening_family from opening_fullname
- Handle missing values safely
- Drop unnecessary columns

Validation Checks

The pipeline performs the following checks:

- Required columns exist in the dataset
- No missing values in critical columns
- No duplicate rows exist
- Valid values in categorical columns (winner)
- Logical constraints are satisfied (e.g., turns >= 1)

Output

The cleaned dataset is saved to:

output/clean_chess.csv

Logging

All pipeline execution logs are stored in:

logs/pipeline.log

Purpose

This project was built for learning and practicing:

- Data engineering pipeline structure
- Data cleaning using Pandas
- Data validation techniques
- Modular Python project design
- Logging and reproducibility

Future Improvements

- Add configuration file for paths
- Add unit testing using pytest
- Add command line interface (CLI)
- Improve logging structure