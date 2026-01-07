import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/processed/bitcoin_cleaned.csv")

# Prophet requires specific column names
df = df[['Date', 'Close']]
df.columns = ['ds', 'y']

# Initialize Prophet model
model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True
)

# Fit model
model.fit(df)

# Create future dataframe (next 30 days)
future = model.make_future_dataframe(periods=30)

# Forecast
forecast = model.predict(future)

# Plot forecast
model.plot(forecast)
plt.title("Bitcoin Price Forecast using Prophet")
plt.show()

# Plot components (trend, seasonality)
model.plot_components(forecast)
plt.show()

# Save forecast
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
    "outputs/prophet_forecast.csv",
    index=False
)

print("Prophet forecasting completed successfully")
