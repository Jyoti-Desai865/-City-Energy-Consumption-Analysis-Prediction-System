import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("city_energy.csv")

# Encode ZoneID (convert text to numbers)
df = pd.get_dummies(df, columns=["ZoneID"], drop_first=True)

# Features (X) and Target (y)
X = df[["AvgTemperature", "Humidity", "SpecialEvent"] + [col for col in df.columns if "ZoneID_" in col]]
y = df["EnergyConsumption"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
print(f"✅ Model trained! Mean Absolute Error (MAE): {mae:.2f} kWh")

# Save model for later use
import joblib
joblib.dump(model, "energy_model.pkl")
print("💾 Model saved as energy_model.pkl")
