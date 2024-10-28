# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('/content/ecommerce_data.csv')

# Print header
print("Printing data header:\n")
print(df.head(10))
print()

# Print data info
print("Printing data info:\n")
print(df.info())
print()

# Print descriptive statistics
print("Printing descriptive statistics:\n")
print(df.describe())
print()

# Check for missing data
print("Checking for missing data:\n")
print(df.isnull().sum())
print()

# Use a for loop to iterate through all quant variables (within a list), removing outliers
quant_var = ['Age', 'Income', 'TotalSpent', 'AvgOrderValue', 'NumOrders',
             'CartAbandonmentRate', 'TimeOnSite', 'Clicks', 'ItemsViewed']

for var in quant_var:
  q75, q25 = np.percentile(df.loc[:, var], [75, 25])
  iqr = q75 - q25
  min_val = q25 - (iqr*1.5)
  max_val = q75 + (iqr*1.5)
  df = df.drop(df[df.loc[:, var] < min_val].index)
  df = df.drop(df[df.loc[:, var] > max_val].index)

# Reprint descriptive statistics
print("Printing updated descriptive statistics:\n")
print(df.describe())
print()

# Histogram showing the distribution of Age
plt.figure(figsize=(10, 5))
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Ages')
plt.show()
print()

# Histogram showing the distribution of Income
plt.figure(figsize=(10, 5))
plt.hist(df['Income'], bins=20, edgecolor='black')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Income Levels')
plt.show()
print()

# Histogram showing the distribution of 'TotalSpent'
plt.figure(figsize=(10, 5))
plt.hist(df['TotalSpent'], bins=20, edgecolor='black')
plt.xlabel('Total Spent ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Total Spent Per Customer')
plt.show()
print()

# Histogram showing the distribution of 'AvgOrderValue'
plt.figure(figsize=(10, 5))
plt.hist(df['AvgOrderValue'], bins=20, edgecolor='black')
plt.xlabel('Average Order Value ($)')
plt.ylabel('Frequency')
plt.title('Distribution of Customer Average Order Values')
plt.show()
print()

# Histogram showing the distribution of 'NumOrders'
plt.figure(figsize=(10, 5))
plt.hist(df['NumOrders'], bins=9, edgecolor='black')
plt.xlabel('Number of Orders')
plt.ylabel('Frequency')
plt.title('Distribution of Number of Orders Per Customer')
plt.show()
print()

# Box plot showing Age by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='Age', data=df)
plt.xlabel('Gender')
plt.ylabel('Age')
plt.title('Age by Gender')
plt.show()
print()

# Box plot showing Income by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='Income', data=df)
plt.xlabel('Gender')
plt.ylabel('Income ($)')
plt.title('Income by Gender')
plt.show()
print()

# Box plot showing 'TotalSpent' by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='TotalSpent', data=df)
plt.xlabel('Gender')
plt.ylabel('Total Spent ($)')
plt.title('Total Spent by Gender')
plt.show()
print()

# Box plot showing AvgOrderValue by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='AvgOrderValue', data=df)
plt.xlabel('Gender')
plt.ylabel('Average Order Value ($)')
plt.title('Average Order Value by Gender')
plt.show()
print()

# Box plot showing NumOrders by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='NumOrders', data=df)
plt.xlabel('Gender')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Gender')
plt.show()
print()

# Box plot showing CartAbandonmentRate by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='CartAbandonmentRate', data=df)
plt.xlabel('Gender')
plt.ylabel('Cart Abandonment Rate')
plt.title('Cart Abandonment Rate by Gender')
plt.show()
print()

# Box plot showing TimeOnSite by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='TimeOnSite', data=df)
plt.xlabel('Gender')
plt.ylabel('Time On Site (Minutes)')
plt.title('Time On Site by Gender')
plt.show()
print()

# Box plot showing Clicks by Gender
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='Clicks', data=df)
plt.xlabel('Gender')
plt.ylabel('Number of Clicks')
plt.title('Number of Clicks by Gender')
plt.show()
print()

# Box plot showing ItemsViewed
plt.figure(figsize=(10, 5))
sns.boxplot(x='Gender', y='ItemsViewed', data=df)
plt.xlabel('Gender')
plt.ylabel('Number of Items Viewed')
plt.title('Number of Items Viewed by Gender')
plt.show()
print()

# Visualize correlation matrix
# Create subset of dataframe without categorical variable 'Gender'
df_corr = df.drop('Gender', axis=1)
corr_matrix = df_corr.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
print()

# Scatterplot showing the relationship between 'Income' and 'TotalSpent'
# Show confidence interval in addition to the line
plt.figure(figsize=(10, 5))
plt.scatter(df['Income'], df['TotalSpent'], alpha=0.5)
plt.xlabel('Income ($)')
plt.ylabel('Total Spent ($)')
plt.title('Income vs. Total Spent')
plt.plot(np.unique(df['Income']), np.poly1d(np.polyfit(df['Income'], df['TotalSpent'], 1))(np.unique(df['Income'])), color='red')
plt.show()
print()

# Scatterplot showing the relationship between 'Income' and 'AvgOrderValue'
plt.figure(figsize=(10, 5))
plt.scatter(df['Income'], df['AvgOrderValue'], alpha=0.5)
plt.xlabel('Income ($)')
plt.ylabel('Average Order Value ($)')
plt.title('Income vs. Average Order Value')
plt.plot(np.unique(df['Income']), np.poly1d(np.polyfit(df['Income'], df['AvgOrderValue'], 1))(np.unique(df['Income'])), color='red')
plt.show()
print()

# Scatterplot showing the relationship between 'TotalSpent' and 'AvgOrderValue'
plt.figure(figsize=(10, 5))
plt.scatter(df['TotalSpent'], df['AvgOrderValue'], alpha=0.5)
plt.xlabel('Total Spent ($)')
plt.ylabel('Average Order Value ($)')
plt.title('Total Spent vs. Average Order Value')
plt.plot(np.unique(df['TotalSpent']), np.poly1d(np.polyfit(df['TotalSpent'], df['AvgOrderValue'], 1))(np.unique(df['TotalSpent'])), color='red')
plt.show()
print()

# Bar plot showing average Age by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='Age', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Age')
plt.title('Average Age by Gender')
plt.show()
print()

# Bar plot showing average Income by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='Income', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Income ($)')
plt.title('Average Income by Gender')
plt.show()
print()

# Bar plot showing average TotalSpent by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='TotalSpent', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Total Spent ($)')
plt.title('Average Total Spent by Gender')
plt.show()
print()

# Bar plot showing average AvgOrderValue by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='AvgOrderValue', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Order Value ($)')
plt.title('Average Order Value by Gender')
plt.show()
print()

# Bar plot showing average NumOrders by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='NumOrders', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Number of Orders')
plt.title('Average Number of Orders by Gender')
plt.show()
print()

# Bar plot showing average CartAbandonmentRate by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='CartAbandonmentRate', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Cart Abandonment Rate')
plt.title('Average Cart Abandonment Rate by Gender')
plt.show()
print()

# Bar plot showing average TimeOnSite by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='TimeOnSite', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Time On Site (Minutes)')
plt.title('Average Time On Site by Gender')
plt.show()
print()

# Bar plot showing average Clicks by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='Clicks', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Number of Clicks')
plt.title('Average Number of Clicks by Gender')
plt.show()
print()

# Bar plot showing average ItemsViewed by Gender
plt.figure(figsize=(10, 5))
sns.barplot(x='Gender', y='ItemsViewed', data=df, errorbar=None)
plt.xlabel('Gender')
plt.ylabel('Average Number of Items Viewed')
plt.title('Average Number of Items Viewed by Gender')
plt.show()
print()
