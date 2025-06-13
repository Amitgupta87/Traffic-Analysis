import pandas as pd

# Load the dataset into a DataFrame
data = pd.read_csv('I94_traffic_data.csv')

# Inspect the data structure
data.head()
# Checking for missing values
data.isnull().sum()

# Handling missing values (if necessary)
data = data.fillna(method='ffill')

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])
import matplotlib.pyplot as plt

# Extract hour from datetime
data['hour'] = data['date'].dt.hour

# Group by hour and calculate the mean traffic volume
traffic_by_hour = data.groupby('hour')['traffic_volume'].mean()

# Plot traffic volume by hour
plt.figure(figsize=(10, 5))
traffic_by_hour.plot(kind='line', color='blue')
plt.title('Average Traffic Volume by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Traffic Volume')
plt.grid(True)
plt.show()
# Extract day of the week
data['day_of_week'] = data['date'].dt.day_name()

# Group by day of the week and calculate the mean traffic volume
traffic_by_day = data.groupby('day_of_week')['traffic_volume'].mean()

# Plot traffic volume by day of the week
plt.figure(figsize=(10, 5))
traffic_by_day.plot(kind='bar', color='orange')
plt.title('Average Traffic Volume by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Traffic Volume')
plt.grid(True)
plt.show()
# Group by weather conditions and calculate mean traffic volume
traffic_by_weather = data.groupby('weather')['traffic_volume'].mean()

# Plot traffic volume by weather condition
plt.figure(figsize=(12, 6))
traffic_by_weather.plot(kind='bar', color='green')
plt.title('Average Traffic Volume by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Traffic Volume')
plt.grid(True)
plt.show()
# Correlation between different features and traffic volume
correlations = data.corr()
correlations['traffic_volume'].sort_values(ascending=False)