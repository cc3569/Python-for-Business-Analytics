# Import library
import pandas as pd

# Load supply chain dataset and print header
df = pd.read_csv('/content/supply_chain_data.csv')
print(df.head(10))
print()

# Print descriptive statistics for supply chain data
print("Descriptive statistics for supply chain data:")
print(df.describe())
print()

# Use nunique to show counts for unique values for data frame by variable
print("Counts for unique values for data frame by variable:")
print(df.nunique())
print()

# Show unique categories of product without the count
print("Unique categories of product:")
print(df['Product'].unique())
print()

# Print unique values for products with the count
print("Unique values for products with the count:")
print(df['Product'].value_counts())
print()

# Show unique categories of warehouse location without the count
print("Warehouse locations:")
print(df['Warehouse_Location'].unique())
print()

# Print unique values for warehouse locations with the count
print("Unique values for warehouse locations with the count:")
print(df['Warehouse_Location'].value_counts())
print()

# Show unique categories of customer without the count
print("Unique customers:")
print(df['Customer'].unique())
print()

# Print unique values for customers with the count
print("Unique values for customers with the count:")
print(df['Customer'].value_counts())
print()

# Print data set info, check for missing values, and clean data if needed
print("Data set info:")
print(df.info())
print()

print("Missing values?")
print(df.isnull().sum())
print()

# Convert 'Order_Date' and 'Shipment_Date' to date-time data type
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Shipment_Date'] = pd.to_datetime(df['Shipment_Date'])

# Print data set info again to check data types
print("Data set info after date-time conversion:")
print(df.info())
print()

# Perform basic data analysis to gain additional insights

# Calculate total sales by multiplying 'Order_Quantity' and 'Price_Per_Unit'
# Add a new variable to dataframe 'Total_Sales'
df['Total_Sales'] = df['Order_Quantity'] * df['Price_Per_Unit']

# Print descriptive statistics for 'Total_Sales'
print("Descriptive statistics for 'Total_Sales':")
print(df['Total_Sales'].describe())
print()

# Show total sales per product descending by 'Total_Sales'
print("Total sales per product:")
total_sales_per_product = df.groupby('Product')['Total_Sales'].sum()
print(total_sales_per_product.sort_values(ascending=False))
print()

# Show total sales by warehouse location descending by 'Total_Sales'
print("Total sales by warehouse location:")
total_sales_per_warehouse = df.groupby('Warehouse_Location')['Total_Sales'].sum()
print(total_sales_per_warehouse.sort_values(ascending=False))
print()

# Show top five customers by total sales
print("Top 5 customers by total sales:")
top_five_customers = df.groupby('Customer')['Total_Sales'].sum()
print(top_five_customers.sort_values(ascending=False).head(5))
print()

# Calculate the average supplier rating per product in descending order
print("Average supplier rating per product:")
average_supplier_rating = df.groupby('Product')['Supplier_Rating'].mean()
print(average_supplier_rating.sort_values(ascending=False))
print()

# Determine the most common product ordered in each warehouse location
print("Most common product ordered in each location:")
most_common_product_per_warehouse = df.groupby('Warehouse_Location')['Product'].agg(pd.Series.mode)
print(most_common_product_per_warehouse)
