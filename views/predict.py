import streamlit as st
import requests

st.title("🔮 Predict Credit Default")

st.markdown("Fill out the form below to predict the likelihood of a customer defaulting on their next payment.")

# --- User Inputs ---
st.header("📋 Financial Info")
limit_bal = st.number_input("Credit Limit (LIMIT_BAL)", min_value=0, step=1000)
pay_0 = st.selectbox("Repayment Status (PAY_0)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_2 = st.selectbox("Repayment Status (PAY_2)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_3 = st.selectbox("Repayment Status (PAY_3)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_4 = st.selectbox("Repayment Status (PAY_4)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_5 = st.selectbox("Repayment Status (PAY_5)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_6 = st.selectbox("Repayment Status (PAY_6)", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
pay_amt1 = st.number_input("Last Payment (PAY_AMT1)", min_value=0, step=100)
pay_amt2 = st.number_input("Payment Two Months Ago (PAY_AMT2)", min_value=0, step=100)
pay_amt4 = st.number_input("Payment Four Months Ago (PAY_AMT4)", min_value=0, step=100)
model_choice = st.selectbox("Model to Use", options=["tuned_random_forest", "tuned_xgboost"])
# --- Model Selection ---
# model_choice = st.selectbox("Model to Use", options=["tuned_random_forest", "tuned_xgboost"])

# --- Prepare Payload ---
input_data = {
    "LIMIT_BAL": limit_bal,
    "PAY_0": pay_0,
    "PAY_2": pay_2,
    "PAY_3": pay_3,
    "PAY_4": pay_4,
    "PAY_5": pay_5,
    "PAY_6": pay_6,
    "PAY_AMT1": pay_amt1,
    "PAY_AMT2": pay_amt2,
    "PAY_AMT4": pay_amt4,
    "model": model_choice
}

# --- Predict ---
if st.button("Predict"):
    try:
        api_url = "http://127.0.0.1:8000/predict"
        response = requests.post(api_url, json=input_data)
        response.raise_for_status()
        prediction = response.json().get("prediction", "N/A")
        st.success(f"🎯 Prediction: {'Default' if prediction == 1 else 'No Default'}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
