import pandas as pd

df = pd.read_csv("export_etab_20250202.csv", sep=';')

print(df.columns.tolist())
print(df.head())