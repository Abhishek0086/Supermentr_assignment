# Assignment 8: Data Doctor

## Overview
A data cleaning and preprocessing tool that handles missing values, duplicates, and standardizes data.

## Features
- **Handle Missing Values**: Fill missing data with mean (numeric) or default values (categorical)
- **Remove Duplicates**: Eliminate duplicate rows
- **Standardize Text**: Convert to proper case and uppercase
- **Save Cleaned Data**: Export cleaned dataset to CSV

## Cleaning Steps
1. Fill missing Age, Marks, Attendance with column mean
2. Fill missing Department with "Unknown"
3. Remove duplicate rows
4. Standardize Name (title case) and Department (uppercase)

## Requirements
- Python 3.x
- Pandas library

## Installation
```bash
pip install pandas
```

## Usage
```bash
python Data_Doctor.py
```

Ensure `student_dirty_data.csv` is in the same directory.

## Output
- Displays original data
- Displays cleaned data
- Saves cleaned data as `cleaned_student_data_v2.csv`

## Concepts Covered
- Data cleaning techniques
- Handling missing values
- Data standardization
- Pandas data manipulation

## Data Quality Issues Addressed
- Missing values
- Duplicate records
- Inconsistent text formatting
