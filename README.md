# Spotify Song Popularity Prediction

This project aims to predict the popularity of Spotify songs in 2024 based on various features such as streaming counts, playlist reach, and social media engagement. A `RandomForestRegressor` model is used to predict the target variable, which is the 'Spotify Popularity' feature.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Data Visualization](#data-visualization)
- [Data Preprocessing](#data-preprocessing)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Evaluation Metrics](#model-training-and-evaluation)

## Overview

This repository contains code that processes Spotify song data, builds a machine learning model to predict song popularity, and evaluates the model's performance.

The key tasks include:
1. Data visualization
2. Data cleaning and preprocessing
3. Feature selection and encoding
4. Model training using `RandomForestRegressor`
5. Model evaluation using multiple metrics

## Getting Started

To get started with this project, ensure you have Python 3.x installed along with the following dependencies:

`pip install pandas seaborn matplotlib scikit-learn`

## Data Visualization
To better understand the dataset before modeling, the following visualizations highlights dataset key patterns: 

**Fig1. Artist vs Spotify Playlist Reach by Albums**

![Artist vs Spotify Playlist Reach by Albums](results/Artist%20vs%20Spotify%20Playlist%20Reach%20by%20Albums.png)
This scatter plot visualizes the relationship between artists and their respective Spotify Playlist Reach - each point represents an album, colored according to its name. The The y-axis displays each album’s playlist reach -  indicating how many unique Spotify users potentially exposed via curated playlists.

**Fig2. Artist vs Spotify Popularity by Albums**

![Artist vs Spotify Popularity by Albums](results/Artist%20vs%20Spotify%20Popularity%20by%20Albums.png)
The second bar chart compares the Spotify popularity score of different artists and their respective albums. The popularity score is a Spotify metric ranging from 0 to 100 that reflects the recent streaming performance of an artist.

**Fig3. Correlation Heatmap of Features**

![Correlation Heatmap of Features](results/Correlation%20Heatmap%20of%20Features.png)
The heatmap provides insight into the correlation between digitial engagement and streaming metrics across platforms (Spotify, YouTube, TikTok, Apple Music, etc), to help identify which features are most interelated.

Details source code can refer to [here](notebooks/main_EDA.ipynb)


## Data Modeling

### Data Preprocessing
The data is loaded from a CSV file, and several preprocessing steps are performed:

1. Handling Missing Values:
Columns with over 50% missing values are dropped.
Rows with missing 'Spotify Popularity' values are also removed.
2. Feature Encoding:
Categorical features (like 'Artist') are encoded using LabelEncoder to make them suitable for machine learning models.
3. Data Cleaning:
Comma characters in object-type columns are removed.
The remaining columns are converted to numeric values.


### Model Training and Evaluation
**1. Training the Model:**
The dataset is split into training and testing sets (80% train, 20% test).
A RandomForestRegressor model is trained using the training data.

**2. Model Evaluation:**
The model is evaluated using the following metrics:
* Mean Absolute Error (MAE): 5.545894736842105
* Mean Squared Error (MSE): 107.55582842105264
* Root Mean Squared Error (RMSE): 10.370912612738218
* R² Score: 0.6259828267292307

Below figure shows the model evaluation results: 

![Artist vs Spotify Popularity by Albums](results/True%20Values%20vs%20Predicted%20Values.png)

The model's predictions are evaluated (and visualized) using a scatter plot comparing the `true Spotify Popularity values` (x-axis) vs. the `predicted values` (y-axis). A red 45-degree line indicates the perfect predictions - points near the linw how accurate results, while devidation reflects prediction errors. The plot demostrates reasonable alignment, particularly for mid-to-high popularity tracks. 


Details source code can refer to [here](notebooks/main_train.ipynb)

### Future Improvements
Here are some potential improvements for future iterations of the project:

* Hyperparameter Tuning: Use GridSearchCV or RandomizedSearchCV to tune hyperparameters and improve model performance.
* Cross-Validation: Implement cross-validation to ensure the model generalizes well to unseen data.
* Feature Importance: Visualize and interpret feature importances to understand which variables contribute most to predictions.
* Model Comparison: Test other regression models (e.g., GradientBoostingRegressor, XGBoost) to compare performance.
