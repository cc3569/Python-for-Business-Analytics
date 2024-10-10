# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
data = pd.read_csv('/content/dc_bike_share.csv')

# Create a histogram showing the distribution of registered bike riders.
plt.hist(data['registered'], bins=30)
plt.xlabel('Number of Registered Bike Riders')
plt.ylabel('Frequency')
plt.title('Distribution of Registered Bike Riders')
plt.show()
print()

# Subset data for 2011 and 2012 separately
data_2011 = data[data['yr'] == 0]
data_2012 = data[data['yr'] == 1]

# Group median number of registered riders by month
median_2011 = data_2011.groupby('mnth')['registered'].median()
median_2012 = data_2012.groupby('mnth')['registered'].median()

# Gather all unique month observations
month = data['mnth'].unique()

# Create a bar plot showing the median number of registered bike riders grouped
# by month for 2011
plt.bar(month, median_2011)
plt.xlabel('Month')
plt.ylabel('Median Number of Registered Bike Riders')
plt.title('Median Number of Registered Bike Riders by Month (2011)')
plt.show()

# Create a bar plot showing the median number of registered bike riders grouped
# by month for 2012
plt.bar(month, median_2012)
plt.xlabel('Month')
plt.ylabel('Median Number of Registered Bike Riders')
plt.title('Median Number of Registered Bike Riders by Month (2012)')
plt.show()

# Gather all unique hour observations
hour = data['hr'].unique()

# Subset data to only include July across 2011 and 2012
july = data[data['mnth'] == 7]

# Group by hour, showing median values
median_july = july.groupby('hr')['registered'].median()

# Create a bar plot showing the median number of registered bike riders by
# hour for the month of July across both years
plt.bar(hour, median_july)
plt.xlabel('Hour')
plt.ylabel('Median Number of Registered Bike Riders')
plt.title('Median Number of Registered Bike Riders by Hour (July)')
plt.show()

# Gather all unique weekday observations
weekday = data['weekday'].unique()

# Group by weekday, showing median values
median_weekday = data.groupby('weekday')['registered'].median()

# Create a bar plot showing the median number of registered bike riders by
# weekday across all years
plt.bar(weekday, median_weekday)
plt.xlabel('Weekday')
plt.ylabel('Median Number of Registered Bike Riders')
plt.title('Median Number of Registered Bike Riders by Weekday')
plt.show()

# Subset data for March 2011
march_2011_data = data[(data['mnth'] == 3) & (data['yr'] == 0)]

# Show scatterplot showing the relationship between 'windspeed' and
# 'registered'
# Add line of best fit to scatterplot
plt.scatter(march_2011_data['windspeed'], march_2011_data['registered'])
plt.xlabel('Windspeed')
plt.ylabel('Number of Registered Bike Riders')
plt.title('Relationship Between Windspeed and Number of Registered Bike Riders (March 2011)')
plt.show()
