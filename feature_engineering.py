import pandas as pd

# Load your cleaned dataset
df = pd.read_csv('uber_clean.csv')  # Make sure this file exists

# Ensure datetime conversion
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day
df['month'] = df['pickup_datetime'].dt.month
df['day_of_week'] = df['pickup_datetime'].dt.day_name()  # e.g., Monday

# Peak time indicator (7-9 AM, 5-7 PM)
df['peak_time'] = df['hour'].apply(
    lambda x: 1 if (7 <= x <= 9) or (17 <= x <= 19) else 0
)

# Encode categorical variables - CORRECTED
df_encoded = pd.get_dummies(df, columns=['day_of_week'], drop_first=True)

# Save enhanced dataset
df_encoded.to_csv('uber_enhanced.csv', index=False)
print("Enhanced dataset with new features saved.")
print(f"New columns: {list(df_encoded.columns)}")