# 🚗📈 Tesla TSLA Stock Price Predictor

---

## 📝 Project Overview  
This project is a web application built using Streamlit that predicts the next day's closing price of Tesla (TSLA) stock. It leverages a pre-trained LSTM deep learning model to provide stock price predictions based on historical data.

---

## ✨ Features  
- 📊 **Historical Data Visualization:**  
  Displays Tesla's historical stock closing prices from 2015 to present with interactive Matplotlib charts.

- 🤖 **Next Day Price Prediction:**  
  Uses last 60 days of closing prices to predict the next trading day's closing price using an LSTM model.

- 🖥️ **User Interface:**  
  Clean and interactive UI with a "Predict Tomorrow's Price" button powered by Streamlit.

---

## ⚙️ How It Works  
1. ⬇️ Downloads Tesla stock data via yfinance.  
2. 🔢 Processes last 60 days of data, scaling for model input.  
3. 🧠 Uses LSTM model to predict scaled closing price.  
4. 🔄 Transforms prediction back to original scale.  
5. 📢 Displays prediction with educational disclaimer.

---

## 🛠️ Technologies Used  
- Python 🐍  
- Streamlit 💻  
- TensorFlow / Keras 🧠  
- yfinance 📉  
- NumPy, Pandas 📊  
- Matplotlib 📈  
- Joblib 🔧  

---

## 🚀 Usage  
- Run the app locally or on the cloud with model and scaler files.  
- View historical stock data.  
- Click "Predict Tomorrow's Price" to see the prediction.

---

## ⚠️ Disclaimer  
This app is for educational purposes only. Stock predictions are inherently uncertain and should not be used for investment decisions.


