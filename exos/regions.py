import pandas as pd

# ── Correspondance département → région (référentiel officiel 2016) ───────────
DEP_TO_REGION = {
    # Auvergne-Rhône-Alpes
    "01": "Auvergne-Rhône-Alpes", "03": "Auvergne-Rhône-Alpes",
    "07": "Auvergne-Rhône-Alpes", "15": "Auvergne-Rhône-Alpes",
    "26": "Auvergne-Rhône-Alpes", "38": "Auvergne-Rhône-Alpes",
    "42": "Auvergne-Rhône-Alpes", "43": "Auvergne-Rhône-Alpes",
    "63": "Auvergne-Rhône-Alpes", "69": "Auvergne-Rhône-Alpes",
    "73": "Auvergne-Rhône-Alpes", "74": "Auvergne-Rhône-Alpes",
    # Bourgogne-Franche-Comté
    "21": "Bourgogne-Franche-Comté", "25": "Bourgogne-Franche-Comté",
    "39": "Bourgogne-Franche-Comté", "58": "Bourgogne-Franche-Comté",
    "70": "Bourgogne-Franche-Comté", "71": "Bourgogne-Franche-Comté",
    "89": "Bourgogne-Franche-Comté", "90": "Bourgogne-Franche-Comté",
    # Bretagne
    "22": "Bretagne", "29": "Bretagne", "35": "Bretagne", "56": "Bretagne",
    # Centre-Val de Loire
    "18": "Centre-Val de Loire", "28": "Centre-Val de Loire",
    "36": "Centre-Val de Loire", "37": "Centre-Val de Loire",
    "41": "Centre-Val de Loire", "45": "Centre-Val de Loire",
    # Corse
    "2A": "Corse", "2B": "Corse",
    # Grand Est
    "08": "Grand Est", "10": "Grand Est", "51": "Grand Est",
    "52": "Grand Est", "54": "Grand Est", "55": "Grand Est",
    "57": "Grand Est", "67": "Grand Est", "68": "Grand Est",
    "88": "Grand Est",
    # Hauts-de-France
    "02": "Hauts-de-France", "59": "Hauts-de-France",
    "60": "Hauts-de-France", "62": "Hauts-de-France", "80": "Hauts-de-France",
    # Île-de-France
    "75": "Île-de-France", "77": "Île-de-France", "78": "Île-de-France",
    "91": "Île-de-France", "92": "Île-de-France", "93": "Île-de-France",
    "94": "Île-de-France", "95": "Île-de-France",
    # Normandie
    "14": "Normandie", "27": "Normandie", "50": "Normandie",
    "61": "Normandie", "76": "Normandie",
    # Nouvelle-Aquitaine
    "16": "Nouvelle-Aquitaine", "17": "Nouvelle-Aquitaine",
    "19": "Nouvelle-Aquitaine", "23": "Nouvelle-Aquitaine",
    "24": "Nouvelle-Aquitaine", "33": "Nouvelle-Aquitaine",
    "40": "Nouvelle-Aquitaine", "47": "Nouvelle-Aquitaine",
    "64": "Nouvelle-Aquitaine", "79": "Nouvelle-Aquitaine",
    "86": "Nouvelle-Aquitaine", "87": "Nouvelle-Aquitaine",
    # Occitanie
    "09": "Occitanie", "11": "Occitanie", "12": "Occitanie",
    "30": "Occitanie", "31": "Occitanie", "32": "Occitanie",
    "34": "Occitanie", "46": "Occitanie", "48": "Occitanie",
    "65": "Occitanie", "66": "Occitanie", "81": "Occitanie",
    "82": "Occitanie",
    # Pays de la Loire
    "44": "Pays de la Loire", "49": "Pays de la Loire",
    "53": "Pays de la Loire", "72": "Pays de la Loire",
    "85": "Pays de la Loire",
    # Provence-Alpes-Côte d'Azur
    "04": "Provence-Alpes-Côte d'Azur", "05": "Provence-Alpes-Côte d'Azur",
    "06": "Provence-Alpes-Côte d'Azur", "13": "Provence-Alpes-Côte d'Azur",
    "83": "Provence-Alpes-Côte d'Azur", "84": "Provence-Alpes-Côte d'Azur",
    # DOM-TOM
    "971": "Guadeloupe", "972": "Martinique", "973": "Guyane",
    "974": "La Réunion",  "976": "Mayotte",
}

def cp_to_region(cp):
    """Extrait le code département depuis le code postal et retourne la région."""
    try:
        cp_str = str(int(float(cp))).zfill(5)   # ex: 7100 → "07100"
    except (ValueError, TypeError):
        return "Inconnu"

    # DOM-TOM : 3 premiers chiffres
    if cp_str[:3] in DEP_TO_REGION:
        return DEP_TO_REGION[cp_str[:3]]

    # Corse : 20x → 2A / 2B (approximation par 200-209 → 2A, 210-219 → 2B)
    if cp_str.startswith("200") or cp_str.startswith("201"):
        return DEP_TO_REGION["2A"]
    if cp_str.startswith("202") or cp_str.startswith("206"):
        return DEP_TO_REGION["2B"]

    # Cas général : 2 premiers chiffres
    dep = cp_str[:2]
    return DEP_TO_REGION.get(dep, "Inconnu")


# ── Chargement ────────────────────────────────────────────────────────────────
df = pd.read_csv(
    "export_etab_20250202.csv",
    sep=";",
    encoding="utf-8-sig",
    dtype=str      # tout en string pour préserver les zéros initiaux
)

# ── Ajout de la colonne Région ────────────────────────────────────────────────
df["Région"] = df["Code postal"].apply(cp_to_region)

# ── Aperçu ────────────────────────────────────────────────────────────────────
print("=== Aperçu des 10 premières lignes (colonnes clés) ===")
print(df[["Département", "Code postal", "Commune", "Région"]].head(10).to_string(index=False))

print("\n=== Répartition par région ===")
print(df["Région"].value_counts().to_string())

print(f"\nTotal établissements : {len(df)}")

# ── Export ────────────────────────────────────────────────────────────────────
df.to_csv("/mnt/user-data/outputs/export_avec_region.csv", sep=";", index=False, encoding="utf-8-sig")
print("\n✓ Fichier exporté : export_avec_region.csv")