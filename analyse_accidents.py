import pandas as pd

df = pd.read_csv("Stats des accidents.csv")

# 1. Infos fichier
print("=== 1. Infos fichier ===")
print(f"Lignes : {df.shape[0]}, Colonnes : {df.shape[1]}")
print(df.dtypes)

# 2. Valeurs manquantes
print("\n=== 2. Valeurs manquantes ===")
print(df.isnull().sum())

# 3. Statistiques descriptives
print("\n=== 3. Statistiques descriptives ===")
print(df.describe())

# 4. Accidents par année
print("\n=== 4. Accidents par année ===")
print(df.groupby("Year").size().reset_index(name="Nombre d'accidents"))

# 5. Accidents par jour
print("\n=== 5. Accidents par jour ===")
print(df.groupby("Day of Week").size().reset_index(name="Nombre d'accidents"))

# 6. Rural vs Urbain
print("\n=== 6. Rural / Urbain ===")
print(df.groupby("Urban/Rural").size().reset_index(name="Nombre d'accidents"))

# 7. Par continent
print("\n=== 7. Par continent ===")
print(df.groupby("Region").size().reset_index(name="Nombre d'accidents"))
