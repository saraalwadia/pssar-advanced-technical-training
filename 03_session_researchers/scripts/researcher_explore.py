import pandas as pd

# Load it
df = pd.read_csv("../raw_data/researchers.csv")

# Understand is
print(df.shape) # (34, 11)
print(df.head()) # [5 rows x 11 columns]
df.dtypes
df.describe()

# Missing values
df.isnull().sum()

# Duplicate values
df.duplicated().sum()

# Explore distributions
df["field"].value_counts()
df["h_index"].describe()

# Filter active researchers
active = df[df["is_active"] == True]
print(active.shape) # (25, 11)