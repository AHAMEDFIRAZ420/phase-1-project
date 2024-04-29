import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('portfolio_data.csv')

# Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)

# Fill missing values if necessary
# data.fillna(method='ffill', inplace=True)

# Handle missing values by dropping rows with missing values
data.dropna(inplace=True)

# Convert date column to datetime format if applicable
# data['Date'] = pd.to_datetime(data['Date'])

# Summary statistics
summary_stats = data.describe()
print("\nSummary Statistics:")
print(summary_stats)

# Data visualization for each dataset
plt.figure(figsize=(12, 8))

# Plot Amazon data
plt.subplot(2, 2, 1)
plt.plot(data['Date'], data['AMZN'], color='b')
plt.title('Amazon Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# Plot DP data
plt.subplot(2, 2, 2)
plt.plot(data['Date'], data['DPZ'], color='g')
plt.title('DPZ Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# Plot BTC data
plt.subplot(2, 2, 3)
plt.plot(data['Date'], data['BTC'], color='r')
plt.title('BTC Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# Plot Netflix data
plt.subplot(2, 2, 4)
plt.plot(data['Date'], data['NFLX'], color='purple')
plt.title('Netflix Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()