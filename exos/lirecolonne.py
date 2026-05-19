import pandas as pd

colonnes = [15]

df = pd.read_csv("export_etab_20250202.csv", sep=';', usecols=colonnes)



print(df)