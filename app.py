import streamlit as st
from src.predict import predict_disease

st.title("AI-Based Drug Repurposing Prediction Model")

st.write("Enter Drug Features")

f1 = st.number_input("Drug Feature 1")
f2 = st.number_input("Drug Feature 2")
f3 = st.number_input("Drug Feature 3")
f4 = st.number_input("Drug Feature 4")

if st.button("Predict Disease Target"):

    result = predict_disease(f1, f2, f3, f4)

    st.success(f"Predicted Disease Target: {result}")