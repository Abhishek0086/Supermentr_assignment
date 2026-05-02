# Assignment 20: Text Cleaner

## Overview
A text preprocessing tool that cleans and normalizes text data for NLP tasks.

## Features
- **Lowercase Conversion**: Convert all text to lowercase
- **Punctuation Removal**: Remove special characters
- **Tokenization**: Split text into words
- **Stop Words Removal**: Filter out common words

## Stop Words Included
Common English words: is, am, are, the, a, an, and, or, in, on, at, to, for, of, with, this

## Requirements
- Python 3.x
- Built-in libraries: `string`

## Usage
```bash
python main.py
```

Enter text when prompted to receive cleaned output.

## Example
```
Input: "This is a sample text with punctuation!"
Output: "sample text punctuation"
```

## Cleaning Steps
1. Convert to lowercase
2. Remove punctuation marks
3. Split into individual words (tokenization)
4. Remove stop words
5. Join cleaned words back together

## Concepts Covered
- Text preprocessing
- Natural Language Processing (NLP)
- Tokenization
- Stop word removal
- Text normalization

## Real-Life Applications
- Sentiment analysis
- Text classification
- Information retrieval
- Machine learning text features

## Customization
You can modify the `stop_words` set to include domain-specific words or add more stop words as needed.
