# STEP 6: Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\us_traffic-accidents\data\traffic_crashes_cleaned.csv"
)

# -----------------------------
# Basic dataset description
# -----------------------------

print("\nDataset Overview:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Distribution of crashes by year
# -----------------------------

crashes_by_year = df["CRASH_YEAR"].value_counts().sort_index()
crashes_by_year.plot(kind="bar")
plt.title("Number of Crashes per Year")
plt.xlabel("Year")
plt.ylabel("Number of Crashes")
plt.show()

# -----------------------------
# Weather condition distribution
# -----------------------------

df["WEATHER_CONDITION"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Weather Conditions During Crashes")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Lighting condition distribution
# -----------------------------

df["LIGHTING_CONDITION"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Lighting Conditions During Crashes")
plt.xlabel("Lighting Condition")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Relationship between speed limit and total injuries
# -----------------------------

df.plot.scatter(x="POSTED_SPEED_LIMIT", y="INJURIES_TOTAL")
plt.title("Speed Limit vs Total Injuries")
plt.xlabel("Speed Limit")
plt.ylabel("Total Injuries")
plt.show()
