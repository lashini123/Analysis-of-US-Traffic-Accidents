# STEP 5: Load sample dataset and perform data cleaning

import pandas as pd

# Load sample dataset
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\us_traffic-accidents\data\traffic_crashes_sample.csv"
)

# Convert CRASH_DATE to datetime
df["CRASH_DATE"] = pd.to_datetime(df["CRASH_DATE"], errors="coerce")

# Remove invalid dates
df = df.dropna(subset=["CRASH_DATE"])

# Fix invalid numeric values
df = df[df["POSTED_SPEED_LIMIT"] >= 0]
df = df[df["INJURIES_TOTAL"] >= 0]
df = df[df["INJURIES_FATAL"] >= 0]

# Standardize text columns
text_columns = [
    "TRAFFIC_CONTROL_DEVICE",
    "WEATHER_CONDITION",
    "LIGHTING_CONDITION",
    "FIRST_CRASH_TYPE",
    "TRAFFICWAY_TYPE",
    "ROADWAY_SURFACE_COND",
    "CRASH_TYPE"
]

for col in text_columns:
    df[col] = df[col].str.strip().str.upper()

# Create new time features
df["CRASH_YEAR"] = df["CRASH_DATE"].dt.year
df["CRASH_MONTH"] = df["CRASH_DATE"].dt.month
df["CRASH_DAY"] = df["CRASH_DATE"].dt.day

# Save cleaned dataset
df.to_csv(
    r"C:\Users\Asus\Desktop\us_traffic-accidents\data\traffic_crashes_cleaned.csv",
    index=False
)

print("Cleaning completed.")
print("Cleaned dataset shape:", df.shape)
