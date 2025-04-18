# Weather Data Analysis and Temperature Prediction

This repository contains a Python script (`script.py`) that performs weather data analysis and predicts the next day's maximum temperature. It utilizes the pandas library for data manipulation, matplotlib for visualization, and scikit-learn for building a linear regression model.

## Overview

The script reads weather data from a CSV file (`weather.csv`), cleans and preprocesses the data, engineers new features, trains a Ridge regression model to predict the next day's maximum temperature, and provides interactive visualizations of the data and predictions.

## Key Features

* **Data Loading and Exploration:** Reads weather data from a CSV file and displays initial information and missing value percentages.
* **Data Cleaning:** Handles missing values by removing columns with excessive missing data (snow-related), filling missing precipitation with 0, and forward-filling missing temperature values.
* **Feature Engineering:** Creates new features such as the 30-day rolling average of the maximum temperature (`month_max`), the ratio of the monthly average to the daily maximum temperature (`month_day_max`), and the ratio of the maximum to minimum daily temperature (`max_min`).
* **Time Series Handling:** Converts the date index to datetime objects and shifts the maximum temperature column to create a target variable for next-day prediction.
* **Model Training:** Trains a Ridge regression model using selected weather features to predict the `target` variable.
* **Model Evaluation:** Calculates and prints the Mean Squared Error of the predictions on a test dataset.
* **Interactive Visualization:** Offers a command-line menu to visualize:
    * Historical maximum and minimum temperatures.
    * Historical precipitation.
    * Predicted versus actual maximum temperatures using different sets of predictor variables.

## Prerequisites

Before running the script, ensure you have the following Python libraries installed:

* **pandas:** For data manipulation and analysis.
* **matplotlib:** For creating plots and visualizations.
* **scikit-learn:** For the Ridge regression model and evaluation metrics.

You can install these libraries using pip:
```
pip install pandas matplotlib scikit-learn
```
Additionally, you need to have the weather.csv file in the same directory as the Python script.
Usage

    Clone the repository (if you have this script in a GitHub repository):
    Bash
```
git clone <repository_url>
cd <repository_name>
```
Ensure the weather.csv file is in the same directory as the Python script.

Run the Python script:
Bash

    python script.py

    Follow the on-screen menu to select the visualizations you want to see. Enter the corresponding number (1, 2, 3, or 4) and press Enter.

Data Source

The script assumes the weather data is stored in a CSV file named weather.csv. The CSV file should have at least the following columns, with a "DATE" column that can be used as an index:

    DATE: Date of the weather observation.
    PRCP: Precipitation.
    SNOW: Snowfall.
    SNWD: Snow depth.
    TMAX: Maximum temperature.
    TMIN: Minimum temperature.

Model Details

The script uses a Ridge regression model with an alpha value of 0.1. Ridge regression is a linear model that adds an L2 penalty to the least squares objective, which helps to prevent overfitting, especially when dealing with potentially correlated predictor variables.
Potential Improvements

   More sophisticated feature engineering: Explore other time-based features (e.g., day of the year, lagged temperature values).
   Different machine learning models: Experiment with other regression algorithms like Linear Regression, Support Vector Regression, or time series models like ARIMA or Prophet.
   Hyperparameter tuning: Optimize the alpha value for the Ridge regression model using techniques like cross-validation.
   More comprehensive error analysis: Investigate the residuals and identify patterns in the prediction errors.
   Saving the trained model: Persist the trained model to avoid retraining it every time the script is run.
   Clearer plotting: Add more descriptive labels, titles, and potentially save the generated plots.
   Error handling: Implement more robust error handling for file reading and user input.

Author

Aravind Anilraj (Phi5ic)
