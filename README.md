# Breast cancer quality report

## Project description
A Python project for assessing data quality in the Wisconsin breast cancer dataset using pandas. It generates summary statistics and checks for missing values and duplicate rows.

## Features
* Missing-value counts and percentages
* Unique-value counts and percentages
* Descriptive statistics, including mean, standard deviation, and quartiles
* Duplicate-row count
* Class balance summary for malignant and benign cases
* CSV export of the quality report

## Project structure
* src/ - analysis and reporting code
* tests/ - automated tests
* data/ - data related documentation
* reports/ - generated CSV reports


## Requirements
* python: >= 3.14
* pandas
* NumPy
* scikit-learn

### Used for development/testing
* pytest

## Setup
Create and activate a virtual environment, then install the project dependencies.

## Usage
Run the analysis script from the project root. The generated reports are saved in the reports/ directory.

## Testing
Run the test suite from the project root:

'python -m pytest'
