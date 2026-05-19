import pandas as pd

df = pd.read_csv("Stats des accidents.csv")

# Renommage colonnes -> snake_case
df.columns = [
    "country", "year", "month", "day_of_week", "time_of_day",
    "urban_rural", "road_type", "weather_conditions", "visibility_level",
    "nb_vehicles", "speed_limit", "driver_age_group", "driver_gender",
    "driver_alcohol_level", "driver_fatigue", "vehicle_condition",
    "pedestrians_involved", "cyclists_involved", "accident_severity",
    "nb_injuries", "nb_fatalities", "emergency_response_time",
    "traffic_volume", "road_condition", "accident_cause",
    "insurance_claims", "medical_cost", "economic_loss",
    "region", "population_density"
]

# Encodage ordinal : mois
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]
df["month_num"] = pd.Categorical(df["month"], categories=month_order, ordered=True).codes + 1

# Encodage ordinal : jour
day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
df["day_num"] = pd.Categorical(df["day_of_week"], categories=day_order, ordered=True).codes + 1

# Encodage ordinal : tranche horaire
time_order = ["Morning","Afternoon","Evening","Night"]
df["time_of_day_num"] = pd.Categorical(df["time_of_day"], categories=time_order, ordered=True).codes + 1

# Encodage ordinal : sévérité
severity_order = ["Minor","Moderate","Severe"]
df["accident_severity_num"] = pd.Categorical(df["accident_severity"], categories=severity_order, ordered=True).codes + 1

# Encodage ordinal : état véhicule
condition_order = ["Poor","Moderate","Good"]
df["vehicle_condition_num"] = pd.Categorical(df["vehicle_condition"], categories=condition_order, ordered=True).codes + 1

# Encodage ordinal : tranche d'âge conducteur
age_order = ["<18","18-25","26-40","41-60","61+"]
df["driver_age_group_num"] = pd.Categorical(df["driver_age_group"], categories=age_order, ordered=True).codes + 1

# Colonne binaire : accident mortel
df["is_fatal"] = (df["nb_fatalities"] > 0).astype(int)

# Colonne binaire : alcool impliqué
df["alcohol_involved"] = (df["driver_alcohol_level"] > 0).astype(int)

# Colonne : coût total
df["total_cost"] = df["medical_cost"] + df["economic_loss"]

# Réorganisation : colonnes texte d'abord, numériques ensuite
text_cols = [
    "country", "region", "year", "month", "month_num",
    "day_of_week", "day_num", "time_of_day", "time_of_day_num",
    "urban_rural", "road_type", "road_condition", "weather_conditions",
    "driver_age_group", "driver_age_group_num", "driver_gender",
    "driver_fatigue", "alcohol_involved", "driver_alcohol_level",
    "vehicle_condition", "vehicle_condition_num",
    "accident_severity", "accident_severity_num",
    "accident_cause", "is_fatal"
]
num_cols = [
    "speed_limit", "nb_vehicles", "visibility_level", "traffic_volume",
    "population_density", "pedestrians_involved", "cyclists_involved",
    "nb_injuries", "nb_fatalities", "emergency_response_time",
    "insurance_claims", "medical_cost", "economic_loss", "total_cost"
]
df = df[text_cols + num_cols]

output_dir = "data/clean"

df.to_csv(f"{output_dir}/accidents_clean.csv", index=False, encoding="utf-8-sig")
df.to_excel(f"{output_dir}/accidents_clean.xlsx", index=False, engine="openpyxl")

print(f"CSV  -> {output_dir}/accidents_clean.csv")
print(f"XLSX -> {output_dir}/accidents_clean.xlsx")
print(f"Lignes : {df.shape[0]} | Colonnes : {df.shape[1]}")
