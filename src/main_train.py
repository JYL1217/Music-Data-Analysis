#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import warnings as w
import os

# Suppress warnings
w.filterwarnings('ignore')

# Get current working directory and its parent directory
root_path = os.getcwd()
parent_directory = os.path.dirname(root_path)
print("Root directory path:", parent_directory)

# Load dataset
df = pd.read_csv(parent_directory + '/data/Most Streamed Spotify Songs 2024.csv', encoding='latin1')

# Calculate missing value counts and their ratio
missing_counts = df.isna().sum()
missing_ratios = missing_counts / len(df)

# Set missing value threshold (50%) and drop columns exceeding this threshold
threshold = 0.5
df_cleaned = df.drop(columns=missing_ratios[missing_ratios > threshold].index)

# Drop rows where 'Spotify Popularity' is missing
df = df_cleaned.dropna(subset=['Spotify Popularity'])

# Fill remaining missing values with the most frequent value (mode) of each column
df.fillna(df.mode().iloc[0], inplace=True)

# Check remaining missing values (for reference/debugging)
df.isna().sum()

# Remove commas from object-type columns and convert to numeric types where possible
df_cleaned = df.apply(lambda x: x.replace({',': ''}, regex=True) if x.dtype == 'object' else x)
df_cleaned = df_cleaned.apply(pd.to_numeric, errors='coerce')

# Feature-label separation: drop non-numeric and non-informative columns
X = df_cleaned.drop(columns=[
    'Spotify Popularity', 'Release Date', 'ISRC',
    'Track', 'Album Name', 'Explicit Track'
])
y = df_cleaned['Spotify Popularity']

from sklearn.preprocessing import StandardScaler, LabelEncoder

# Encode categorical 'Artist' column as numeric values
label_encoder = LabelEncoder()
X['Artist'] = label_encoder.fit_transform(X['Artist'])

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regressor model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Evaluate model performance
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred)}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred)}")
print(f"Root Mean Squared Error (RMSE): {mean_squared_error(y_test, y_pred, squared=False)}")
print(f"R^2 Score: {r2_score(y_test, y_pred)}")

# Plot predicted vs actual values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)  # 45-degree reference line
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True Values vs Predicted Values')
plt.show()
