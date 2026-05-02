# Assignment 13: House Price Predictor

## Overview
A linear regression model that predicts house prices based on area.

## Purpose
Demonstrates supervised learning for price prediction using a simple linear relationship.

## How It Works
1. Load house data (area and price)
2. Train a linear regression model
3. Accept user input for house area
4. Predict the price based on the trained model

## Requirements
- Python 3.x
- Pandas library
- Scikit-learn library

## Installation
```bash
pip install pandas scikit-learn
```

## Usage
```bash
python main.py
```

Ensure `dataset.csv` is in the same directory.

## Example
```
Enter house area: 2000
Predicted House Price: ₹5,000,000.00
```

## Dataset Format
CSV file with columns:
- `Area`: House area in square feet
- `Price`: House price in rupees

## Concepts Covered
- Linear regression
- Supervised learning
- Model training and prediction
- Feature-target relationship

## Real-Life Applications
- Real estate price estimation
- Property valuation
- Market analysis
- Investment decisions

## Model Limitations
- Assumes linear relationship between area and price
- Works best with similar properties
- May not account for other factors (location, amenities, etc.)
