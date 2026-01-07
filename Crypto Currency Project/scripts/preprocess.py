import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/bitcoin_raw.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Remove missing values
df.dropna(inplace=True)

# Sort by date (very important for time series)
df = df.sort_values('Date')

# Save cleaned data
df.to_csv("data/processed/bitcoin_cleaned.csv", index=False)

print("Data preprocessing completed successfully")
print(df.head())
