# Assignment 22: Movie Review Analyzer

## Overview
A rule-based sentiment analyzer that classifies movie reviews as positive, negative, or neutral based on word matching.

## How It Works
1. Convert review text to lowercase and split into words
2. Count positive and negative words
3. Compare counts to determine sentiment
4. Return sentiment classification with emoji

## Sentiment Classification
- **Positive 😊**: More positive words than negative
- **Negative 😞**: More negative words than positive
- **Neutral 😐**: Equal positive and negative words

## Word Lists
**Positive Words**: good, great, amazing, awesome, love, excellent, fantastic, nice

**Negative Words**: bad, worst, boring, terrible, hate, awful, poor, waste

## Requirements
- Python 3.x
- No external libraries needed

## Usage
```bash
python main.py
```

## Example Output
```
Review 1: This movie was amazing and awesome
Sentiment: Positive 😊

Review 2: Worst movie ever it was boring
Sentiment: Negative 😞

Review 3: The film was good but a bit slow
Sentiment: Neutral 😐
```

## Concepts Covered
- Sentiment analysis
- Rule-based classification
- Text processing
- Natural Language Processing (NLP)

## Real-Life Applications
- Movie/product review analysis
- Customer feedback classification
- Social media monitoring
- Brand sentiment tracking

## Limitations
- Simple word matching (doesn't understand context)
- No handling of negations (e.g., "not good")
- Limited word vocabulary
- Doesn't consider word intensity

## Improvements for Advanced Version
- Use negation handling (not, no, never)
- Implement TF-IDF weighting
- Add more comprehensive word lists
- Use machine learning models (Naive Bayes, SVM)
- Implement aspect-based sentiment analysis
- Handle emojis and emoticons
