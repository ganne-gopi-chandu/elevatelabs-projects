# apst.py

import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("xgboost_model.pkl")

st.set_page_config(page_title="Credit Card Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection")

st.markdown("Enter values for V1–V28 and normalized transaction amount (normAmount).")

features = []

# Input fields for V1–V28
for i in range(1, 29):
    features.append(st.number_input(f"V{i}", value=0.0))

# Normalized amount input
normAmount = st.number_input("Normalized Amount", value=0.0)
features.append(normAmount)

# Prediction
if st.button("Predict"):
    prediction = model.predict([features])[0]
    if prediction == 1:
        st.error("🚨 Fraud Detected")
    else:
        st.success("✅ Transaction is Normal")

