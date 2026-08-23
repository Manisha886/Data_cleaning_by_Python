# Data_cleaning_by_Python
# Cafe Sales Data Cleaning & Data Quality Analysis with Python

## Project Overview

This project demonstrates an end-to-end data cleaning and data quality workflow using Python and Pandas on a messy cafe sales dataset.

The objective is to identify missing, invalid, inconsistent, and duplicate data; convert columns into appropriate data types; reconstruct derived transaction values where possible; validate the cleaned dataset; and prepare the data for reliable downstream analysis.

This project focuses on practical data-cleaning techniques that are commonly used in Data Analyst and Data Science workflows.

---

## Business Problem

Raw business data often contains missing values, incorrect data types, inconsistent categorical values, duplicate records, and invalid numerical values.

For a cafe sales dataset, these issues can affect important business metrics such as:

- Total sales
- Average transaction value
- Product performance
- Payment-method analysis
- Sales trends
- Customer and location analysis

The goal of this project is to transform the raw dataset into a cleaner and more reliable dataset suitable for analysis.

---

## Dataset

The project uses a cafe sales dataset containing transaction-level information.

### Main Columns

| Column | Description |
|---|---|
| Transaction ID | Unique identifier for a transaction |
| Item | Product purchased |
| Quantity | Number of units purchased |
| Price Per Unit | Price of one unit |
| Total Spent | Total transaction amount |
| Payment Method | Payment method used |
| Location | Transaction location |
| Transaction Date | Date of the transaction |

The original dataset is stored as:

`dirty_cafe_sales.csv`

The cleaned dataset is generated as:

`cleaned_cafe_sales.csv`

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Data Cleaning Workflow

The project follows these major steps:

### 1. Initial Data Inspection

The raw dataset was inspected using:

- `df.info()`
- `df.describe()`
- `df.shape`
- `df.isnull().sum()`
- Missing-value percentages
- Duplicate checks
- Frequency analysis of categorical variables

This helped identify potential data-quality issues before modifying the data.

---

### 2. Missing-Value Analysis

Missing values were identified across the dataset and their proportion was calculated.

Categorical fields such as:

- Item
- Payment Method
- Location

were inspected separately to understand the missing-value patterns.

---

### 3. Handling Invalid Values

Some columns contained values such as:

- `UNKNOWN`
- `ERROR`

These values were identified and handled appropriately before performing numerical calculations.

---

### 4. Data Type Conversion

Numerical columns were converted into appropriate numeric data types using Pandas.

For example:

```python
df['Price Per Unit'] = pd.to_numeric(
    df['Price Per Unit'],
    errors='coerce'
)


