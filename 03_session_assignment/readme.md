# Project Overview

This project is a data pipeline built as part of a technical training program.
It demonstrates how to integrate, clean, and analyze multiple heterogeneous datasets related to researchers, publications, and funding.

The goal is to transform raw data from different formats (CSV, JSON, Excel) into a unified analytical dataset and extract meaningful insights.

## Datasets

The project uses three data sources:

- Researchers (CSV) → basic information about researchers
- Publications (JSON) → publications and citations data
- Funding (Excel) → funding amounts per researcher
Data Pipeline Workflow

## The pipeline follows these steps:

Load Data → Merge Datasets → Clean Data → Analyze → Save Output
1. Data Loading

Data is loaded from different formats:

CSV using pandas.read_csv
JSON using json.load + pd.json_normalize
Excel using pandas.read_excel

All datasets are unified using a consistent project base path.

2. Data Merging

Two types of joins were performed:

- Inner Join
Keeps only matching records across all datasets
Result: 49 rows
- Left Join
Keeps all researchers even if missing related data
Result: 86 rows

Data Loss
Rows lost in inner join: 37 rows
These represent researchers missing publications or funding data.

3. Data Cleaning
A reusable function clean_funding(df) was implemented to clean funding data:

- Cleaning steps:
Convert funding values to numeric format
Remove commas from numbers
Handle invalid values (converted to NaN)
Remove negative or zero funding values

4. Final Dataset

After merging cleaned datasets:

Final dataset shape: (86, 23)

This dataset combines researchers, publications, and funding into a single analytical table.

## Key Insights
1. Top Researcher by Citations
Researcher R001 has the highest total citations
Total citations: 20660
2. Most Funded Field
The field Data Engineering received the highest funding
Total funding: 960,000 CAD
3. Earliest Active Researcher
Researcher R026 is the earliest active researcher
Joined in: 2006

## Output
The final cleaned dataset is saved at:
output/clean_research_data.csv

## Key Learnings
This project demonstrates:
- Handling multi-format data (CSV, JSON, Excel)
- Merging datasets using relational keys
- Differences between inner vs left join
- Data cleaning techniques for numerical fields
- Basic analytical aggregation using pandas
- Building a simple but complete data pipeline

## Technologies Used
Python
Pandas
JSON handling
File system management (os)