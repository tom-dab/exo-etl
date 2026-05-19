import pandas as pd

# ── 1. Chargement du fichier ──────────────────────────────────────────────────
df = pd.read_csv("export_etab_20250202.csv", sep=';')

colonne = "Nombre d'étudiants"

# ── 2. Nettoyage : suppression des valeurs nulles et négatives ────────────────
serie = pd.to_numeric(df[colonne], errors="coerce")   # convertit en numérique
serie_valide = serie[serie > 0].dropna()              # exclut NaN et <= 0

# ── 3. Calcul des statistiques ────────────────────────────────────────────────
somme   = serie_valide.sum()
moyenne = serie_valide.mean()
minimum = serie_valide.min()
maximum = serie_valide.max()

# ── 4. Affichage ──────────────────────────────────────────────────────────────
print("=" * 45)
print(f"  Statistiques — « {colonne} »")
print("=" * 45)
print(f"  Lignes totales      : {len(serie)}")
print(f"  Valeurs valides     : {len(serie_valide)}")
print(f"  Valeurs exclues     : {len(serie) - len(serie_valide)}")
print("-" * 45)
print(f"  Somme               : {somme:,.0f}")
print(f"  Moyenne             : {moyenne:,.2f}")
print(f"  Minimum             : {minimum:,.0f}")
print(f"  Maximum             : {maximum:,.0f}")
print("=" * 45)