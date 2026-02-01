import pandas as pd

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()

print("COLUMNS:", list(df.columns))
print(df.head())
