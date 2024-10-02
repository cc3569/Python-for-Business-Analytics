# Import necessary libraries
import pandas as pd

# Import data
df = pd.read_csv('/content/consumer_income.csv')

# Print header, shpwing first 10 records
print("Header:")
print(df.head(10))
print(df.shape)
print()

# Check for missing data
print("Missing Data:")
print(df.isnull().sum())
print(df.shape)
print()

# Remove missing 'Income' data values from dataframe
print("Removed missing Income values...")
df = df.dropna(subset=['Income'])
print(df.isnull().sum())
print(df.shape)
print()

# Print all unique 'Education' categories and counts
print("Education Levels:")
print(df['Education'].value_counts())
print()

# Print all unique 'Marital_Status' categories and counts
print("Marital Statuses:")
print(df['Marital_Status'].value_counts())
print()

# Print descriptive statistics
print("Descriptive Statistics: ")
print(df.describe().round(4))
print()

# Create an 'Age' column using this year and the 'Year_Birth' column
from datetime import datetime
current_year = datetime.now().year
df['Age'] = current_year - df['Year_Birth']
print(df.describe())
print()

# Print the data sorted by income in descending order
print("Sorted by Income:")
income_descending = df.sort_values(by='Income', ascending=False)
print(income_descending.head(10))
print()

# Drop the highest income outlier and print the data sorted by income
df = df.drop(2233, axis=0)
print("Sorted by Income (without outlier):")
income_descending = df.sort_values(by='Income', ascending=False)
print(income_descending.head(10))
print()

# Print descriptive statistics
print("Descriptive Statistics (without outlier):")
print(df.describe().round(4))
print()

# Show median income levels for each 'Education' level
print("Median Income by Education Level:")
print(df.groupby('Education')['Income'].median().sort_values(ascending=False))
print()

# Show median income levels for each 'Marital_Status'
print("Median Income by Marital Status:")
print(df.groupby('Marital_Status')['Income'].median().sort_values(ascending=False))
print()

# Add a column 'Total_Children' that sums 'Kidhome' and 'Teenhome' columns
# Print descriptive statistics for 'Total_Children' only
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
print("Descriptive Statistics for 'Total_Children':")
print(df['Total_Children'].describe().round(4))
print()

# Subset data to include only those with two or more 'Total_Children'
print("Data with two or more 'Total_Children':")
two_or_more = df[df['Total_Children'] >= 2]
print(two_or_more.describe())
print()
