import yfinance as yf
import pandas as pd

btc = yf.download("BTC-USD", start="2022-01-01")

btc.reset_index(inplace=True)
btc.to_csv("data/raw/bitcoin_raw.csv", index=False)

print("Bitcoin data downloaded successfully")
