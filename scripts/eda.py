# STEP 3: Insight-Driven Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(
    r"C:\Users\Asus\Desktop\us_traffic-accidents\data\traffic_crashes_cleaned.csv"
)

# -------------------------------------
# Q1: How have crashes changed over time?
# -------------------------------------

crashes_per_year = df.groupby("CRASH_YEAR").size()
crashes_per_year.plot(kind="line", marker="o")
plt.title("Traffic Crashes Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Crashes")
plt.show()

# -------------------------------------
# Q2: Are there seasonal crash patterns?
# -------------------------------------

crashes_per_month = df.groupby("CRASH_MONTH").size()
crashes_per_month.plot(kind="line", marker="o")
plt.title("Traffic Crashes Per Month")
plt.xlabel("Month")
plt.ylabel("Number of Crashes")
plt.show()

# -------------------------------------
# Q3: Weather condition impact
# -------------------------------------

df["WEATHER_CONDITION"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Weather Conditions During Crashes")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.show()

# -------------------------------------
# Q4: Lighting condition impact
# -------------------------------------

df["LIGHTING_CONDITION"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Lighting Conditions During Crashes")
plt.xlabel("Lighting Condition")
plt.ylabel("Count")
plt.show()

# -------------------------------------
# Q5: Speed limit vs injury severity
# -------------------------------------

df.plot.scatter(x="POSTED_SPEED_LIMIT", y="INJURIES_TOTAL")
plt.title("Speed Limit vs Total Injuries")
plt.xlabel("Posted Speed Limit")
plt.ylabel("Total Injuries")
plt.show()

# -------------------------------------
# Q6: Distribution of injury counts
# -------------------------------------

plt.hist(df["INJURIES_TOTAL"], bins=30)
plt.title("Distribution of Total Injuries")
plt.xlabel("Total Injuries")
plt.ylabel("Frequency")
plt.show()

# -------------------------------------
# Q7: Injury outliers
# -------------------------------------

plt.boxplot(df["INJURIES_TOTAL"])
plt.title("Outliers in Injury Counts")
plt.ylabel("Total Injuries")
plt.show()

# -------------------------------------
# Q8: Crash type frequency
# -------------------------------------

df["CRASH_TYPE"].value_counts().head(10).plot(kind="bar")
plt.title("Most Common Crash Types")
plt.xlabel("Crash Type")
plt.ylabel("Count")
plt.show()
