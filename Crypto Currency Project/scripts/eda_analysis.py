import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/processed/bitcoin_cleaned.csv")

# Convert Date
df['Date'] = pd.to_datetime(df['Date'])

# ===============================
# 1. Price Trend
# ===============================
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'])
plt.title("Bitcoin Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# ===============================
# 2. Trading Volume
# ===============================
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Volume'], color='orange')
plt.title("Bitcoin Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# ===============================
# 3. Daily Returns
# ===============================
df['Daily_Return'] = df['Close'].pct_change()

plt.figure(figsize=(10,5))
sns.histplot(df['Daily_Return'].dropna(), bins=50)
plt.title("Distribution of Daily Returns")
plt.show()
