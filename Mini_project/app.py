# app.py - Your Streamlit Web Application

import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow.keras.models import load_model
import joblib
import matplotlib.pyplot as plt

# Load the trained model and scaler
@st.cache_resource
def load_assets():
    model = load_model('tesla_stock_predictor.h5')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_assets()

# Set up the Streamlit page
st.set_page_config(page_title="Tesla Stock Predictor", page_icon="📈")
st.title('📈 Tesla (TSLA) Stock Price Predictor')
st.markdown("This app uses a trained LSTM model to predict Tesla's stock price and visualize historical data.")

# --- Fetch and Display Historical Data ---
st.header("Historical Stock Data")
# Download historical data
df = yf.download('TSLA', start='2015-01-01', end=pd.to_datetime('today').strftime('%Y-%m-%d'))

# Display data and chart
st.write("Displaying data for the last few years:")
st.dataframe(df.tail())

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['Close'], label='Close Price')
ax.set_title('Tesla Close Price History')
ax.set_xlabel('Date')
ax.set_ylabel('Price (USD)')
ax.grid(True)
st.pyplot(fig)


# --- Prediction Section ---
st.header("Predict the Next Day's Closing Price")

# Explain the process to the user
st.markdown("""
To predict tomorrow's closing price, the model needs the last 60 days of closing prices.
The button below will fetch the latest data and run the prediction.
""")

if st.button('Predict Tomorrow\'s Price'):
    with st.spinner('Fetching data and making prediction...'):
        # 1. Fetch the last 60 days of data
        last_60_days = df['Close'][-60:].values
        
        # 2. Scale the data
        last_60_days_scaled = scaler.transform(last_60_days.reshape(-1, 1))
        
        # 3. Create the test sample
        X_pred = []
        X_pred.append(last_60_days_scaled)
        X_pred = np.array(X_pred)
        
        # 4. Reshape for the model
        X_pred = np.reshape(X_pred, (X_pred.shape[0], X_pred.shape[1], 1))
        
        # 5. Make the prediction
        pred_price_scaled = model.predict(X_pred)
        
        # 6. Inverse transform the prediction
        pred_price = scaler.inverse_transform(pred_price_scaled)
        
        # Display the result
        st.success(f"Predicted Closing Price for the Next Trading Day: **${pred_price[0][0]:.2f}**")

st.markdown("---")
st.write("Disclaimer: This is a project for educational purposes. Stock market predictions are inherently uncertain. Do not use for financial decisions.")