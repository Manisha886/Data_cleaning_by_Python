import pandas as pd
import numpy as np

#  import matplotlib.pyplot as plt
df=pd.read_csv('dirty_cafe_sales.csv')
df
df.info()
df.describe().round()
df.isnull().sum()
df.shape
df.isnull().sum()/len(df)*100
df[df.duplicated()].shape
df['Transaction ID'].value_counts().head(10)
# Check frequency distribution and missing values for key categorical columns
# Frequency analysis of payment methods and locations (including NaNs)
print("Value counts for 'Payment Method':")
df['Payment Method'].value_counts(dropna=False)

print("\nValue counts for 'Location':")
df['Location'].value_counts(dropna=False)
# As 'UNKNOWN' is already a category in both columns, I will fill the missing `NaN` values with 'UNKNOWN' to maintain consistency in the dataset.
df['Payment Method'] = df['Payment Method'].fillna('UNKNOWN')
df['Location'] = df['Location'].fillna('UNKNOWN')
# Verify that missing values have been filled
print("Missing values after imputation:")
df[['Payment Method', 'Location']].isnull().sum()
# similarly we can fill the missing values 
print("Value counts for 'Item':")
df['Item'].value_counts(dropna=False)

print("\nValue counts for 'Quantity':")
df['Quantity'].value_counts(dropna=False)
# Fill missing values in 'Item' column
# Fill NaN values with 'UNKNOWN'.
df['Item'] = df['Item'].fillna('UNKNOWN')

print("Value counts for 'Item' after imputation:")
df['Item'].value_counts(dropna=False)
# Clean and fill missing values in 'Price Per Unit' column
#  Replace 'UNKNOWN' and 'ERROR' with NaN
df['Price Per Unit'] = df['Price Per Unit'].replace({'UNKNOWN': np.nan, 'ERROR': np.nan})

# Convert 'Price Per Unit' to numeric, coercing errors to NaN
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')

# Calculate the mode for imputation
price_per_unit_mode = df['Price Per Unit'].mode()[0]

# Fill NaN values with the mode
df['Price Per Unit'] = df['Price Per Unit'].fillna(price_per_unit_mode)

print("Value counts for 'Price Per Unit' after imputation:")
df['Price Per Unit'].value_counts(dropna=False)

print("Missing values for 'Price Per Unit' after imputation:")
df['Price Per Unit'].isnull().sum()

print("Value counts for 'Price Per Unit':")
df['Price Per Unit'].value_counts(dropna=False)

print("\nData type of 'Price Per Unit':")
df['Price Per Unit'].dtype
# Clean and fill missing values in 'Quantity' column
# Replace 'UNKNOWN' and 'ERROR' with NaN
df['Quantity'] = df['Quantity'].replace({'UNKNOWN': np.nan, 'ERROR': np.nan})

# Convert 'Quantity' to numeric, coercing errors to NaN
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Calculate the mode for imputation
quantity_mode = df['Quantity'].mode()[0]

# Fill NaN values with the mode
df['Quantity'] = df['Quantity'].fillna(quantity_mode)

print("Value counts for 'Quantity' after imputation:")
df['Quantity'].value_counts(dropna=False)

print("Missing values for 'Item' and 'Quantity' after imputation:")
df[['Item', 'Quantity']].isnull().sum()

# Clean and fill missing values in 'Total Spent' column
#First, convert non-numeric string values ('UNKNOWN', 'ERROR') and current NaN values to numerical NaN
# Then, where possible, recalculate 'Total Spent' using 'Quantity' and 'Price Per Unit'
# Finally, impute any remaining NaN values with the mode of the column
# Replace 'UNKNOWN' and 'ERROR' with NaN, and convert to numeric
df['Total Spent'] = df['Total Spent'].replace({'UNKNOWN': np.nan, 'ERROR': np.nan})
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')

# Recalculate 'Total Spent' where it's NaN and Quantity/Price Per Unit are available
recalculated_total_spent = df['Quantity'] * df['Price Per Unit']
mask = df['Total Spent'].isnull()
df.loc[mask, 'Total Spent'] = recalculated_total_spent.loc[mask]

# Calculate the mode for imputation for any remaining NaN values
total_spent_mode = df['Total Spent'].mode()[0]

# Fill remaining NaN values with the mode
df['Total Spent'] = df['Total Spent'].fillna(total_spent_mode)

print("Value counts for 'Total Spent' after imputation:")
df['Total Spent'].value_counts(dropna=False)

print("Missing values for 'Total Spent' after imputation:")
df['Total Spent'].isnull().sum()

print("Value counts for 'Total Spent':")
df['Total Spent'].value_counts(dropna=False)

print("\nData type of 'Total Spent':")
df['Total Spent'].dtype

# Clean and fill missing values in 'Transaction Date' column
# Replace 'UNKNOWN' and 'ERROR' with NaN
df['Transaction Date'] = df['Transaction Date'].replace({'UNKNOWN': np.nan, 'ERROR': np.nan})

# Convert 'Transaction Date' to datetime, coercing errors to NaN
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# Calculate the mode for imputation
transaction_date_mode = df['Transaction Date'].mode()[0]

# Fill NaN values with the mode
df['Transaction Date'] = df['Transaction Date'].fillna(transaction_date_mode)

print("Value counts for 'Transaction Date' after imputation:")
df['Transaction Date'].value_counts(dropna=False)

print("Missing values for 'Transaction Date' after imputation:")
df['Transaction Date'].isnull().sum()

print("Value counts for 'Transaction Date':")
df['Transaction Date'].value_counts(dropna=False)

print("\nData type of 'Transaction Date':")
df['Transaction Date'].dtype
# After all cleaning steps, let's check the final state of the DataFrame
df.info()

# After all cleaning steps, we can save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_cafe_sales.csv', index=False)
print("Cleaned DataFrame saved to 'cleaned_cafe_sales.csv'")
