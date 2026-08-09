import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("Mobile Price Prediction System")
st.write("Enter mobile specifications to predict price range.")

col1, col2 = st.columns(2)

with col1:
    battery_power = st.number_input("Battery Power (mAh)", min_value=0, value=1000)
    clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.0, value=1.5, step=0.1)
    fc = st.number_input("Front Camera (MP)", min_value=0, value=5)
    int_memory = st.number_input("Internal Memory (GB)", min_value=0, value=32)
    m_dep = st.number_input("Mobile Depth (cm)", min_value=0.0, value=0.5, step=0.1)
    n_cores = st.number_input("Number of Cores", min_value=1, value=4)
    pc = st.number_input("Primary Camera (MP)", min_value=0, value=10)
    px_height = st.number_input("Pixel Height", min_value=0, value=800)
    px_width = st.number_input("Pixel Width", min_value=0, value=1200)
    ram = st.number_input("RAM (MB)", min_value=0, value=2000)

with col2:
    sc_h = st.number_input("Screen Height (cm)", min_value=0, value=12)
    sc_w = st.number_input("Screen Width (cm)", min_value=0, value=6)
    talk_time = st.number_input("Talk Time (hours)", min_value=0, value=10)
    blue = st.selectbox("Bluetooth", ["Yes", "No"])
    dual_sim = st.selectbox("Dual SIM", ["Yes", "No"])
    four_g = st.selectbox("4G", ["Yes", "No"])
    three_g = st.selectbox("3G", ["Yes", "No"])
    touch_screen = st.selectbox("Touch Screen", ["Yes", "No"])
    wifi = st.selectbox("WiFi", ["Yes", "No"])
    mobile_wt = st.selectbox("Mobile Weight Category", ["Low", "Med", "High"])

if st.button("Predict"):
    yes_no = lambda v: 1 if v == "Yes" else 0

    row = {
        "battery_power": battery_power,
        "blue": yes_no(blue),
        "clock_speed": clock_speed,
        "dual_sim": yes_no(dual_sim),
        "fc": fc,
        "four_g": yes_no(four_g),
        "int_memory": int_memory,
        "m_dep": m_dep,
        "n_cores": n_cores,
        "pc": pc,
        "px_height": px_height,
        "px_width": px_width,
        "ram": ram,
        "sc_h": sc_h,
        "sc_w": sc_w,
        "talk_time": talk_time,
        "three_g": yes_no(three_g),
        "touch_screen": yes_no(touch_screen),
        "wifi": yes_no(wifi),
        # one-hot for mobile_wt, matching OneHotEncoder(drop="first") fit on ["High","Low","Med"] -> baseline "High"
        "mobile_wt_Low": 1 if mobile_wt == "Low" else 0,
        "mobile_wt_Med": 1 if mobile_wt == "Med" else 0,
    }

    input_df = pd.DataFrame([row])
    # Guarantee identical column order to what the model/scaler were fit on
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Price Range: {prediction[0]}")
