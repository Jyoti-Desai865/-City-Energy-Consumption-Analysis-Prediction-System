# City-Energy-Consumption-Analysis-Prediction-System

This project analyzes city-wide electricity consumption patterns and predicts next-day demand using weather conditions, events, and zone-based data. It was developed as part of my Data Science Internship at IBI.

*How to Generate / Load the Dataset:*

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

*OUTPUT:*

<img width="1193" height="806" alt="Image" src="https://github.com/user-attachments/assets/354906b6-6790-4659-a5cd-18723f89e609" />


<img width="905" height="667" alt="Image" src="https://github.com/user-attachments/assets/1d57d85a-4f55-42f0-97bb-9c98f5d3aae4" />


<img width="896" height="656" alt="Image" src="https://github.com/user-attachments/assets/fd1dd037-5644-4e78-8997-05c9edff5c0f" />


<img width="1212" height="201" alt="Image" src="https://github.com/user-attachments/assets/91bc0936-e424-41d5-843b-562a5332bd86" />
