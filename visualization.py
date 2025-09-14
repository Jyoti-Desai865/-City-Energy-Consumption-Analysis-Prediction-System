import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("city_energy.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

# 1. Line chart: Monthly energy usage trends
monthly_trend = df.groupby(["Month"])["EnergyConsumption"].mean()
plt.figure(figsize=(8,5))
plt.plot(monthly_trend.index, monthly_trend.values, marker='o')
plt.title("Monthly Average Energy Consumption (All Zones)")
plt.xlabel("Month")
plt.ylabel("Avg Energy Consumption (kWh)")
plt.grid(True)
plt.show()

# 2. Heatmap: Correlation between features
plt.figure(figsize=(6,4))
corr = df[["AvgTemperature", "Humidity", "SpecialEvent", "EnergyConsumption"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 3. Bar chart: Event vs Non-event average consumption
event_usage = df.groupby("SpecialEvent")["EnergyConsumption"].mean()
plt.figure(figsize=(6,4))
sns.barplot(x=event_usage.index, y=event_usage.values, palette="viridis")
plt.xticks([0,1], ["No Event", "Event"])
plt.title("Average Consumption on Event vs Non-event Days")
plt.ylabel("Avg Energy Consumption (kWh)")
plt.show()
