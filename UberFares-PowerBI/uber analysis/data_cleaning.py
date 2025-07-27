import pandas as pd

print("Loading dataset...")
df = pd.read_csv('uber.csv')

print("\nInitial data inspection:")
print("Rows:", df.shape[0], "Columns:", df.shape[1])
print("\nMissing values:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)

# Basic cleaning
print("\nCleaning data...")
df_clean = df.dropna()
df_clean = df_clean[df_clean['fare_amount'] > 0]
df_clean = df_clean[df_clean['passenger_count'] > 0]

df_clean.to_csv('uber_clean.csv', index=False)
print("\nCleaned data saved. New dimensions:", df_clean.shape)