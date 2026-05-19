import pandas as pd

df = pd.read_csv("exercice5.csv", sep=';')

# 1. Lire et afficher le tableau
print("=== 1. Tableau complet ===")
print(df)

# 2. Afficher les noms de colonnes
print("\n=== 2. Noms de colonnes ===")
print(df.columns.tolist())

# 3. Afficher le type de chaque colonne
print("\n=== 3. Types de chaque colonne ===")
print(df.dtypes)

# 4. Afficher les premières lignes de la colonne NOM
print("\n=== 4. Premières lignes de la colonne NOM ===")
print(df['NOM'].head())

# 5. Afficher les dernières lignes de la colonne NOM
print("\n=== 5. Dernières lignes de la colonne NOM ===")
print(df['NOM'].tail())

# 6. Afficher l'âge maximum
print("\n=== 6. Âge maximum ===")
print(df['AGE 2020'].max())

# 7. Afficher la première valeur de la colonne AGE 2020
print("\n=== 7. Première valeur de AGE 2020 ===")
print(df['AGE 2020'].iloc[0])

# 8. Afficher les 3 premières valeurs de la colonne AGE 2020
print("\n=== 8. Les 3 premières valeurs de AGE 2020 ===")
print(df['AGE 2020'].head(3))

# 9. Afficher AGE 2020 trié par ordre croissant
print("\n=== 9. AGE 2020 trié par ordre croissant ===")
print(df['AGE 2020'].sort_values().reset_index(drop=True))

# 10. Nombre de personnes par ville
print("\n=== 10. Nombre de personnes par ville ===")
print(df['VILLE'].value_counts())