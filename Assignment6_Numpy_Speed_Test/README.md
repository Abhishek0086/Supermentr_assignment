# Assignment 6: NumPy Speed Test

## Overview
A performance comparison between Python lists and NumPy arrays for numerical operations.

## Purpose
Demonstrates why NumPy is preferred for numerical computing by comparing execution times.

## What It Does
- Creates 1 million numbers using both Python list and NumPy array
- Performs multiplication operation on both
- Measures and compares execution time

## Requirements
- Python 3.x
- NumPy library

## Installation
```bash
pip install numpy
```

## Usage
```bash
python Numpy_Speed_Test.py
```

## Expected Output
```
--- Speed Test Results ---
Python List Time: 0.050000 seconds
NumPy Array Time: 0.001000 seconds
```

## Key Takeaway
NumPy arrays are significantly faster than Python lists for numerical operations due to:
- Vectorized operations
- Optimized C implementation
- Contiguous memory layout

## Concepts Covered
- Performance benchmarking
- NumPy arrays vs Python lists
- Time complexity analysis
