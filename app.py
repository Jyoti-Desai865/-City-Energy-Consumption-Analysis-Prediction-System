import pandas as pd
import joblib

# Load trained model
model = joblib.load("energy_model.pkl")

# List of available zones
zones = ["Zone_1", "Zone_2", "Zone_3", "Zone_4", "Zone_5"]

# Ask for user input
print("⚡ City Energy Consumption Prediction System ⚡")

zone = input(f"Enter Zone ID {zones}: ")
while zone not in zones:
    print("❌ Invalid Zone ID! Please choose from:", zones)
    zone = input(f"Enter Zone ID {zones}: ")

try:
    temp = float(input("Enter tomorrow's Avg Temperature (°C): "))
    humidity = float(input("Enter tomorrow's Humidity (%): "))
    event = int(input("Is there a Special Event? (0 = No, 1 = Yes): "))
    if event not in [0, 1]:
        raise ValueError("Event must be 0 or 1")
except ValueError as e:
    print("❌ Invalid input:", e)
    exit()

# Create input dataframe
input_data = {
    "AvgTemperature": [temp],
    "Humidity": [humidity],
    "SpecialEvent": [event],
    "ZoneID_Zone_2": [1 if zone == "Zone_2" else 0],
    "ZoneID_Zone_3": [1 if zone == "Zone_3" else 0],
    "ZoneID_Zone_4": [1 if zone == "Zone_4" else 0],
    "ZoneID_Zone_5": [1 if zone == "Zone_5" else 0],
}

X_new = pd.DataFrame(input_data)

# Prediction
prediction = model.predict(X_new)[0]
print(f"\n🔮 Predicted Energy Consumption for {zone} tomorrow: {prediction:.2f} kWh")
