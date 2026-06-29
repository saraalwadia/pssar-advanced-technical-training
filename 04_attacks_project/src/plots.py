import pandas as pd
import matplotlib.pyplot as plt
import os

# ─────────────────────────────
# 1. Ensure output folder exists
# ─────────────────────────────
os.makedirs("../output/plots", exist_ok=True)

# ─────────────────────────────
# 2. Load cleaned data
# ─────────────────────────────
df = pd.read_csv("../data/processed/attacks_clean.csv")

# ─────────────────────────────
# 3. Bar Chart — Fatal (Y/N)
# ─────────────────────────────
df["Fatal (Y/N)"].value_counts().plot(kind="bar")
plt.title("Fatal (Y/N) Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.savefig("../output/plots/fatal_bar.png")
plt.close()

# ─────────────────────────────
# 4. Scatter Plot — Age vs Year
# ─────────────────────────────
df.plot(kind="scatter", x="Age", y="Year", alpha=0.3)
plt.title("Age vs Year")
plt.savefig("../output/plots/age_scatter.png")
plt.close()

# ─────────────────────────────
# 5. Box Plot — Age distribution
# ─────────────────────────────
df.boxplot(column="Age")
plt.title("Age Distribution")
plt.savefig("../output/plots/age_box.png")
plt.close()

print("All plots saved successfully in output/plots/")