# Import necessary packages
import pandas as pd

# Import dataframe and print header
dataframe = pd.read_csv('/content/flagstaff_real_estate_data.csv')
print("Dataframe:\n")
print(dataframe.head())

# Print Descriptive Statistics
print("\nFlagstaff Real Estate Data Descriptive Statistics:\n")
print(dataframe.describe())

# Prints Median Home Price for the Dataset
print(f"\nFlagstaff Overall Median Home Price: ${dataframe['PRICE'].median():.0f}\n")

# Prints median home prices grouped by year
print(f"Flagstaff Median Home Price by Year:\n")
print(dataframe.groupby('YEAR')['PRICE'].median())

# Subsets data based on 2010-2019 using loc method (2022 is the recent)
subset = dataframe.loc[(dataframe['YEAR'] >= 2010) & (dataframe['YEAR'] <= 2019)]

# Prints descriptive statistics for subset data
print("\nFlagstaff Real Estate Data Descriptive Statistics (2010-2019):\n")
print(subset.describe())

# Prints overall median price for subset data
print(f"\nFlagstaff Overall Median Home Price (2010-2019): ${subset['PRICE'].median():.0f}")

# Group subset home price data by year
print("\nFlagstaff Median Home Price by Year (2010-2019):\n")
print(subset.groupby('YEAR')['PRICE'].median())
