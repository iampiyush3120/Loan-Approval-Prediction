import streamlit as st
import joblib
import numpy as np

import os

model_path = os.path.join(os.path.dirname(__file__), "..", "Model", "loan_model.pkl")
model = joblib.load(model_path)

st.title("🏦 Loan Approval Prediction")

st.write("Enter Applicant Details")

dependents = st.number_input("Number of Dependents", value=0)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["No", "Yes"])
income = st.number_input("Annual Income", value=500000)
loan_amount = st.number_input("Loan Amount", value=1000000)
loan_term = st.number_input("Loan Term", value=12)
cibil = st.number_input("CIBIL Score", value=700)
res_asset = st.number_input("Residential Assets", value=0)
com_asset = st.number_input("Commercial Assets", value=0)
lux_asset = st.number_input("Luxury Assets", value=0)
bank_asset = st.number_input("Bank Assets", value=0)

education = 0 if education == "Graduate" else 1
self_emp = 0 if self_emp == "No" else 1

if st.button("Predict"):

    data = np.array([[
        dependents,
        education,
        self_emp,
        income,
        loan_amount,
        loan_term,
        cibil,
        res_asset,
        com_asset,
        lux_asset,
        bank_asset
    ]])

    prediction = model.predict(data)

    if prediction[0] == 0:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")