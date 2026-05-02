# Assignment 12: KNN in Real Life

## Overview
A K-Nearest Neighbors (KNN) implementation that finds similar users based on their characteristics.

## Purpose
Demonstrates how KNN algorithm works in real-world scenarios like recommendation systems.

## How It Works
1. Load user data from CSV
2. Accept new user input (features)
3. Find 2 nearest neighbors using Euclidean distance
4. Display the most similar users

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
Input: New user with features [5, 1, 1]
Output: Shows 2 most similar users from the dataset
```

## Concepts Covered
- K-Nearest Neighbors algorithm
- Distance metrics (Euclidean)
- Similarity-based recommendations
- Real-world applications

## Real-Life Applications
- Movie/product recommendations
- User similarity detection
- Anomaly detection
- Classification tasks

## Dataset Format
CSV file with user features and a User identifier column.
