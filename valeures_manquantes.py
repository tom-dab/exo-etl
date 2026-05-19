import pandas as pd
from datetime import datetime

df = pd.read_csv("data/clean/accidents_clean.csv")

total_rows = len(df)
total_cells = df.size

missing = df.isnull().sum()
missing_pct = (missing / total_rows * 100).round(2)

missing_df = pd.DataFrame({
    "colonne": missing.index,
    "valeurs_manquantes": missing.values,
    "pourcentage": missing_pct.values
}).query("valeurs_manquantes > 0").sort_values("valeurs_manquantes", ascending=False)

total_missing = missing.sum()
cols_with_missing = len(missing_df)

lines = []
lines.append("# Rapport — Valeurs Manquantes\n")
lines.append(f"**Date :** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
lines.append(f"**Source :** `data/clean/accidents_clean.csv`\n")
lines.append("---\n")

lines.append("## Résumé global\n")
lines.append(f"| Indicateur | Valeur |")
lines.append(f"|---|---|")
lines.append(f"| Nombre de lignes | {total_rows:,} |")
lines.append(f"| Nombre de colonnes | {df.shape[1]} |")
lines.append(f"| Total de cellules | {total_cells:,} |")
lines.append(f"| Cellules manquantes | {total_missing:,} |")
lines.append(f"| % manquant global | {round(total_missing / total_cells * 100, 2)} % |")
lines.append(f"| Colonnes avec valeurs manquantes | {cols_with_missing} |")
lines.append("")

if cols_with_missing == 0:
    lines.append("## Détail par colonne\n")
    lines.append("> **Aucune valeur manquante** dans le dataset. Le fichier est complet.")
else:
    lines.append("## Détail par colonne\n")
    lines.append("| Colonne | Valeurs manquantes | Pourcentage |")
    lines.append("|---|---|---|")
    for _, row in missing_df.iterrows():
        lines.append(f"| `{row['colonne']}` | {int(row['valeurs_manquantes']):,} | {row['pourcentage']} % |")
    lines.append("")

    lines.append("## Colonnes complètes\n")
    complete_cols = missing[missing == 0].index.tolist()
    lines.append(", ".join([f"`{c}`" for c in complete_cols]))

lines.append("\n---")
lines.append("*Rapport généré automatiquement.*")

report = "\n".join(lines)

with open("rapports/valeurs_manquantes.md", "w", encoding="utf-8") as f:
    f.write(report)

print("Rapport généré : rapports/valeurs_manquantes.md")
print(f"Valeurs manquantes totales : {total_missing}")
print(f"Colonnes concernées : {cols_with_missing}")
