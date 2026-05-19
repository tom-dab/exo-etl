import pandas as pd

df = pd.read_csv("Stats des accidents.csv")

# --- Étape 1 : Informations du fichier ---
print("Infos fichier :")
print(f"\nNb lignes : {df.shape[0]}")
print(f"Nb colonnes : {df.shape[1]}")
print(f"\nColonnes et types de data :")
print(df.dtypes.to_string())
print(f"\n5 premières lignes :")
print(df.head())
