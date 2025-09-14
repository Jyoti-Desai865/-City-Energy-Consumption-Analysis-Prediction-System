import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Create date range for 1 year
dates = pd.date_range(start="2024-01-01", end="2024-12-31")

# Define zones
zones = [f"Zone_{i}" for i in range(1, 6)]  # 5 zones

data = []

for zone in zones:
    for date in dates:
        avg_temp = np.random.normal(30, 5)       # around 30°C ± 5
        humidity = np.random.normal(60, 10)      # around 60% ± 10
        event = np.random.choice([0, 1], p=[0.85, 0.15])  # 15% chance of event
        # Base consumption influenced by temperature, humidity & event
        consumption = (
            200 + avg_temp * 8 + humidity * 2 + event * 100
            + np.random.normal(0, 20)  # random noise
        )
        data.append([date, zone, avg_temp, humidity, event, consumption])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "ZoneID", "AvgTemperature", "Humidity", "SpecialEvent", "EnergyConsumption"])

# Save dataset
df.to_csv("city_energy.csv", index=False)

print("✅ Dataset created successfully! Shape:", df.shape)
print(df.head())
