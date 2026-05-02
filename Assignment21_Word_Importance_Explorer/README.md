# Assignment 21: Word Importance Explorer

## Overview
A TF-IDF (Term Frequency-Inverse Document Frequency) analysis tool that identifies the most important words in documents.

## Purpose
Demonstrates how to extract meaningful features from text data using TF-IDF vectorization.

## How It Works
1. Load sample documents
2. Apply TF-IDF vectorization
3. Extract feature names (words)
4. Identify top 3 most important words for each document
5. Display words with their TF-IDF scores

## Requirements
- Python 3.x
- Scikit-learn library

## Installation
```bash
pip install scikit-learn
```

## Usage
```bash
python main.py
```

## Example Output
```
Document 1:
machine -> 0.577
learning -> 0.577
powerful -> 0.577

Document 2:
deep -> 0.707
learning -> 0.707
subset -> 0.707
```

## Concepts Covered
- TF-IDF vectorization
- Feature extraction from text
- Word importance scoring
- Text analysis

## TF-IDF Explained
- **TF (Term Frequency)**: How often a word appears in a document
- **IDF (Inverse Document Frequency)**: How unique a word is across all documents
- **TF-IDF Score**: Product of TF and IDF - higher score = more important word

## Real-Life Applications
- Search engine ranking
- Document similarity
- Information retrieval
- Text classification
- Keyword extraction

## Stop Words
English stop words are automatically removed during vectorization (the, is, a, etc.)

## Customization
You can modify the documents list to analyze your own text data.
