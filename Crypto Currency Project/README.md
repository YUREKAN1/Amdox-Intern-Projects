Crypto Price Analysis & Forecasting Dashboard

Project Overview:

This project presents an end-to-end data analytics dashboard for analyzing Bitcoin price behavior, risk, and forecasting trends using Power BI.
It combines historical data analysis, technical indicators, time-series forecasting, and performance evaluation to provide actionable insights into cryptocurrency markets.



Objectives:

Analyze historical Bitcoin price movements

Identify market trends and volatility

Forecast future prices using time-series models

Evaluate simple trading strategies

Present insights through interactive dashboards



Tools & Technologies:

Power BI – Data visualization & dashboarding

Python – Data collection & preprocessing

Time-Series Models – ARIMA, Prophet

DAX – Measures, indicators, correlation logic



Project Structure:
├── data/
│   ├── raw/                  # Raw Bitcoin price data
│   ├── processed/            # Cleaned & feature-engineered data
│
├── scripts/
│   ├── data_fetch.py
│   ├── preprocess.py
│   ├── eda_analysis.py
|  
│
├── dashboard/
│   ├── Crypto_Dashboard.pbix  # Power BI dashboard file
│
├── README.md



Dashboard Pages:

Price Overview & Trends

Candlestick & Technical Analysis

Forecast & Uncertainty Analysis

Volatility & Risk Analysis

Interactive Explorer

Indicators Dashboard

Correlations & Market Structure

Feature Importance & Explainability

Strategy Backtest & Performance

Conclusion & Future Scope



Key Features:

Moving Averages (MA7, MA30)

Volatility & Daily Return Analysis

ARIMA & Prophet Forecasting

Forecast Uncertainty Bands

Price–Volume Correlation

Trend-Following Strategy Analysis

Interactive Date Filtering



Key Insights:

Bitcoin exhibits high volatility compared to traditional assets

Trend-following indicators capture major market movements

Prophet model performs better for long-term trend forecasting

Trading volume shows a moderate positive relationship with price

Simple strategies reduce downside risk but underperform in sideways markets



Limitations:

Feature importance is implicit in time-series models

External factors such as news and macroeconomic events are not included

Backtesting results are illustrative and not financial advice



Future Scope:

Integrate sentiment analysis from news and social media

Apply deep learning models (LSTM, Transformers)

Expand analysis to multiple cryptocurrencies

Enable real-time streaming dashboards

Perform advanced strategy backtesting with transaction costs



Disclaimer:

This project is for educational and analytical purposes only and does not constitute financial or investment advice.



Author:
Yurekan M
Data Analytics Enthusiast