# City-Energy-Consumption-Analysis-Prediction-System

This project analyzes city-wide electricity consumption patterns and predicts next-day demand using weather conditions, events, and zone-based data. It was developed as part of my Data Science Internship at IBI.

#How to Generate / Load the Dataset:#

Run first.py to generate a synthetic dataset for 365 days across multiple city zones.
The dataset includes:
Date
Zone ID
Average Temperature
Humidity
Special Events (0/1)
Energy Consumption (kWh)
The dataset will be saved as city_energy.csv.
To load the dataset directly:
import pandas as pd
data = pd.read_csv("city_energy.csv")

*How to Run the Notebook:*

Open Energy_Analysis.ipynb in Jupyter Notebook or VS Code.
Run all cells in order:
Dataset Creation / Loading
Data Preprocessing & Cleaning
Exploratory Data Analysis (EDA)
Visualizations (Line chart, Heatmap, Bar chart)
Model Training (Random Forest)
Prediction of Next-Day Consumption

*Insights from the Analysis:*

Seasonal Usage Patterns → Energy demand is higher in hot months due to cooling needs.
Zone-Level Insights → Each city zone shows different usage behavior.
Impact of Events → Festivals and sports events significantly increase energy consumption.
Weather Correlation → Temperature and humidity strongly affect electricity usage.
Model Performance → Random Forest achieved a Mean Absolute Error (MAE) ≈ 18 kWh.
