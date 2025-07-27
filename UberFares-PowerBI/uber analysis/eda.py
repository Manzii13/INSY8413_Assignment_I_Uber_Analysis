import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('uber_clean.csv')

# Basic statistics
print("Descriptive statistics:\n", df.describe())

# Fare distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['fare_amount'], bins=30, kde=True)
plt.title('Fare Amount Distribution')
plt.savefig('fare_distribution.png')
plt.show()

# Time-based analysis (if datetime converted)
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    df['hour'] = df['pickup_datetime'].dt.hour

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='hour', y='fare_amount', data=df)
    plt.title('Fare Amount by Hour of Day')
    plt.savefig('fare_by_hour.png')
    plt.show()