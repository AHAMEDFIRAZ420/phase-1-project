import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('hack.csv')

# Data cleaning
# Drop rows with missing values
data_cleaned = data.dropna()

# Convert 'ID' column to integer if not already
data_cleaned['ID'] = data_cleaned['ID'].astype(int)

# Convert 'STORECODE' column to string if not already
data_cleaned['STORECODE'] = data_cleaned['STORECODE'].astype(str)

# Convert 'MONTH' column to datetime if not already
data_cleaned['ID'] = pd.to_datetime(data_cleaned['ID'])

# Analyzing the dataset
# Display the first few rows of the cleaned dataset
print("First few rows of the cleaned dataset:")
print(data_cleaned.head())

# Summary statistics
print("\nSummary statistics of the cleaned dataset:")
print(data_cleaned.describe())

# Data visualization
# Example: PLOT of the 'ID' column
plt.figure(figsize=(8, 6))
plt.plot(data_cleaned['ID'])
plt.title('plot of ID')
plt.xlabel('ID')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Example: Bar plot of 'grp' column
plt.figure(figsize=(8, 6))
data_cleaned['GRP'].value_counts().plot(color='orange')
plt.title('Bar Plot of GRP')
plt.xlabel('GRP')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Example: Line plot of 'MONTH' column
plt.figure(figsize=(10, 6))
data_cleaned.groupby('MONTH').size().plot(color='green')
plt.title('Number of Entries by MONTH')
plt.xlabel('MONTH')
plt.ylabel('Count')
plt.grid(True)
plt.show()