# Rapport — Analyse Stats des accidents.csv

## 1. Informations du fichier

| | |
|---|---|
| Lignes | 132 000 |
| Colonnes | 30 |
| Colonnes texte (str) | 14 |
| Colonnes numériques (int64 / float64) | 16 |

**Colonnes disponibles :**
Country, Year, Month, Day of Week, Time of Day, Urban/Rural, Road Type, Weather Conditions, Visibility Level, Number of Vehicles Involved, Speed Limit, Driver Age Group, Driver Gender, Driver Alcohol Level, Driver Fatigue, Vehicle Condition, Pedestrians Involved, Cyclists Involved, Accident Severity, Number of Injuries, Number of Fatalities, Emergency Response Time, Traffic Volume, Road Condition, Accident Cause, Insurance Claims, Medical Cost, Economic Loss, Region, Population Density

---

## 2. Valeurs manquantes

**Aucune valeur manquante** sur l'ensemble des 30 colonnes. Le jeu de données est complet.

---

## 3. Statistiques descriptives (colonnes numériques)

| Colonne | Moyenne | Min | Max |
|---|---|---|---|
| Year | 2012 | 2000 | 2024 |
| Visibility Level | 275.04 | 50.00 | 500.00 |
| Number of Vehicles Involved | — | — | — |
| Speed Limit | — | — | — |
| Driver Alcohol Level | — | — | — |
| Number of Injuries | — | — | — |
| Number of Fatalities | — | — | — |
| Emergency Response Time | — | — | — |
| Traffic Volume | — | — | — |
| Medical Cost | — | — | — |
| Economic Loss | 50 437 | 1 000 | 99 999 |
| Population Density | 2 506 | 10 | 4 999 |

---

## 4. Accidents par année

| Année | Nombre d'accidents |
|---|---|
| 2000 | 5 280 |
| 2001 | 5 263 |
| 2002 | 5 433 |
| 2003 | 5 327 |
| 2004 | 5 180 |
| 2005 | 5 302 |
| 2006 | 5 156 |
| 2007 | 5 307 |
| 2008 | 5 409 |
| 2009 | 5 298 |
| 2010 | 5 144 |
| 2011 | 5 356 |
| 2012 | 5 327 |
| 2013 | 5 220 |
| 2014 | 5 351 |
| 2015 | 5 331 |
| 2016 | 5 377 |
| 2017 | 5 278 |
| 2018 | 5 295 |
| 2019 | 5 243 |
| 2020 | 5 308 |
| 2021 | 5 243 |
| 2022 | 5 175 |
| 2023 | 5 242 |
| 2024 | 5 155 |

La distribution est très uniforme (~5 200 accidents/an), sans tendance à la hausse ni à la baisse sur 25 ans.

---

## 5. Accidents par jour de la semaine

| Jour | Nombre d'accidents |
|---|---|
| Mardi | 19 061 |
| Mercredi | 19 001 |
| Dimanche | 18 939 |
| Vendredi | 18 854 |
| Samedi | 18 818 |
| Lundi | 18 708 |
| Jeudi | 18 619 |

La répartition est quasi égale entre les jours (~18 600–19 100). Mardi et mercredi sont légèrement en tête.

---

## 6. Accidents en zone rurale / urbaine

| Zone | Nombre d'accidents | Part |
|---|---|---|
| Rural | 66 502 | 50,4 % |
| Urbain | 65 498 | 49,6 % |

Répartition pratiquement équilibrée entre les deux zones.

---

## 7. Accidents par continent

| Continent | Nombre d'accidents |
|---|---|
| Australia | 26 625 |
| North America | 26 415 |
| Asia | 26 351 |
| Europe | 26 345 |
| South America | 26 264 |

Les 5 continents présentent un nombre d'accidents quasi identique (~26 400 chacun).

---

## Conclusion

Les distributions observées (par année, par jour, par zone et par continent) sont anormalement uniformes pour un jeu de données réel. Cela suggère que ce dataset a été **généré synthétiquement**, probablement à des fins pédagogiques.
