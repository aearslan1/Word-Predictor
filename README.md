# Word Similarity Predictor

A Python class designed to calculate similarity ratios between a given word and a pool of words using multiple text-matching algorithms.

## Features

*   **Same Word Ratio:** Measures character-level similarity by comparing unique letter sets, ignoring duplicates.
*   **Letter Sequence Ratio:** Compares positional character matches between two strings.
*   **All Ratio:** A weighted combination algorithm (30% letter set, 70% sequence) to provide a final prediction score.
*   **Levenshtein Distance Matrix (WIP):** A framework to calculate the minimum edit distance between strings using matrix operations.

## How It Works

```python
from predictor import EPredictor

# Initialize the predictor with a word pool
epredictor = EPredictor(["berkay", "egemen", "görkem"])
name = "ege"

# Get similarity scores
print(epredictor.allRatio(name))