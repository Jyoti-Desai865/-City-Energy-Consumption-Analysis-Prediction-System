import pandas as pd

# Load dataset
df = pd.read_csv("city_energy.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Extract month
df["Month"] = df["Date"].dt.month

# 1. Average consumption per month per zone
monthly_avg = df.groupby(["ZoneID", "Month"])["EnergyConsumption"].mean().reset_index()
print("📊 Average Monthly Consumption per Zone:")
print(monthly_avg.head(15))

# 2. Correlation analysis
corr = df[["AvgTemperature", "Humidity", "SpecialEvent", "EnergyConsumption"]].corr()
print("\n📈 Correlation Matrix:")
print(corr)
