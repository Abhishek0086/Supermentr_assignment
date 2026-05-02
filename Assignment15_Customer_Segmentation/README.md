# Assignment 15: Customer Segmentation

## Overview
A K-Means clustering model that segments customers into groups based on income and spending behavior.

## Purpose
Demonstrates unsupervised learning for customer segmentation in marketing and business analytics.

## How It Works
1. Load customer data (annual income and spending score)
2. Apply K-Means clustering with 3 clusters
3. Assign each customer to a cluster
4. Display customer groups and their characteristics

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

## Output
- Full dataset with cluster assignments
- Detailed breakdown of each cluster

## Dataset Format
CSV file with columns:
- `Annual Income`: Customer's annual income
- `Spending Score`: Customer's spending behavior score (1-100)

## Concepts Covered
- K-Means clustering
- Unsupervised learning
- Customer segmentation
- Cluster analysis

## Real-Life Applications
- Customer targeting
- Marketing strategy
- Product recommendations
- Customer lifetime value analysis

## Cluster Interpretation
- **Cluster 0**: Low income, low spending
- **Cluster 1**: High income, high spending
- **Cluster 2**: Medium income, medium spending

(Actual interpretation depends on data distribution)
