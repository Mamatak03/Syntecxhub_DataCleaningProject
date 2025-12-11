import pandas as pd
import numpy as np

cleaning_log = []

df = pd.read_csv("raw_dataset.csv")
cleaning_log.append("Loaded dataset: raw_dataset.csv")
cleaning_log.append(f"Initial shape: {df.shape}")

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
cleaning_log.append("Standardized column names.")

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["joindate"] = pd.to_datetime(df["joindate"], errors="coerce", dayfirst=True)

df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["joindate"] = df["joindate"].fillna(df["joindate"].mode()[0])

df = df.drop_duplicates()

df.to_csv("cleaned_dataset.csv", index=False)

with open("cleaning_log.txt", "w") as f:
    for line in cleaning_log:
        f.write(line + "\n")

print("Cleaning complete!")
