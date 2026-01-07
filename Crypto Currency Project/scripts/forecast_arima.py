import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load cleaned data
df = pd.read_csv("data/processed/bitcoin_cleaned.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Use Close price for forecasting
close_prices = df.set_index('Date')['Close']

# Build ARIMA model
model = ARIMA(close_prices, order=(5,1,0))
model_fit = model.fit()

# Forecast next 30 days
forecast = model_fit.forecast(steps=30)

# Create forecast dates
forecast_dates = pd.date_range(
    start=close_prices.index[-1] + pd.Timedelta(days=1),
    periods=30
)

# Plot results
plt.figure(figsize=(10,5))
plt.plot(close_prices, label="Historical Prices")
plt.plot(forecast_dates, forecast, label="Forecast", color='red')
plt.title("Bitcoin Price Forecast using ARIMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# Save forecast
forecast_df = pd.DataFrame({
    "Date": forecast_dates,
    "Forecast_Price": forecast
})

forecast_df.to_csv("outputs/forecast_results.csv", index=False)

print("ARIMA forecasting completed successfully")
