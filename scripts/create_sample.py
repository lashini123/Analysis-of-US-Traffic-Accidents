# STEP 4: Create GitHub-friendly sample dataset from raw file

import pandas as pd

# Load the large raw dataset (never pushed to GitHub)
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\data_sets\Traffic_Crashes.csv",
    low_memory=False
)

# Select useful analysis columns
columns_needed = [
    "CRASH_DATE",
    "POSTED_SPEED_LIMIT",
    "TRAFFIC_CONTROL_DEVICE",
    "WEATHER_CONDITION",
    "LIGHTING_CONDITION",
    "FIRST_CRASH_TYPE",
    "TRAFFICWAY_TYPE",
    "LANE_CNT",
    "ALIGNMENT",
    "ROADWAY_SURFACE_COND",
    "CRASH_TYPE",
    "INJURIES_TOTAL",
    "INJURIES_FATAL"
]

df = df[columns_needed]

# Remove rows with missing critical fields
df = df.dropna(subset=["CRASH_DATE", "WEATHER_CONDITION", "LIGHTING_CONDITION"])

# Create a representative sample
df_sample = df.sample(n=200000, random_state=42)

# Save sample dataset to data folder
df_sample.to_csv(
    r"C:\Users\Asus\Desktop\us_traffic-accidents\data\traffic_crashes_sample.csv",
    index=False
)

print("Sample dataset created.")
print("Shape:", df_sample.shape)
