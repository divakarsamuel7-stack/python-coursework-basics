# Python Coursework Basics

A small collection of Python exercises completed as part of my programming coursework while studying **MSc Agrobioinformatics at Justus Liebig University Giessen**.

The repository focuses on foundational Python concepts that are useful for scientific computing and data analysis.

## Projects

### 1. `enumerate_zip.py` — Working with multiple lists

- Combines three lists using `zip()`.
- Uses `enumerate()` to number each iteration, starting from 1.
- Finds the largest and smallest value in each tuple using `max()` and `min()`.

Run it:

```bash
python enumerate_zip.py
```

### 2. `datasets.py` — Basic statistical calculations

- Reads numerical input from the command line.
- Uses a loop to collect values until the user enters `q`.
- Calculates the number of observations, sum, mean, and sample variance.
- Handles invalid input, empty datasets, and datasets with fewer than two values.

Run it:

```bash
python datasets.py
```

For sample variance, the program uses the denominator `n - 1`, so at least two observations are required.

## Requirements

- Python 3
- No external packages required

## Learning objectives

- Lists and tuples
- `for` and `while` loops
- `zip()` and `enumerate()`
- Conditional statements
- User input and exception handling
- Built-in functions such as `sum()`, `max()`, and `min()`
- Basic descriptive statistics
- Functions and code organisation

## Note

These are educational coursework exercises. The code has been organised and improved for readability and basic input handling while retaining the original learning objectives.

## Author

Divakar Samuel Sasykumar  
MSc Agrobioinformatics, Justus Liebig University Giessen
