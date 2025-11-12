import streamlit as st
import pandas as pd
import plotly.express as px
import time
import random

st.title("Channel Monitoring")

# Mock real-time data (in real use, replace with live telemetry)
def get_live_data():
    return {
        "Channel 1": {"Voltage": 12 + random.uniform(-0.3, 0.3),
                      "Current": random.uniform(0.5, 1.5)},
        "Channel 2": {"Voltage": 12 + random.uniform(-0.3, 0.3),
                      "Current": random.uniform(0.1, 1.0)},
    }

placeholder = st.empty()

for _ in range(5):  # refresh 5 times for demo
    data = get_live_data()
    df = pd.DataFrame([
        [ch, vals["Voltage"], vals["Current"], vals["Voltage"]*vals["Current"]]
        for ch, vals in data.items()
    ], columns=["Channel", "Voltage (V)", "Current (A)", "Power (W)"])
    with placeholder.container():
        cols = st.columns(3)
        cols[0].plotly_chart(px.bar(df, x="Channel", y="Power (W)", title="Power"))
        cols[1].plotly_chart(px.bar(df, x="Channel", y="Voltage (V)", title="Voltage"))
        cols[2].plotly_chart(px.bar(df, x="Channel", y="Current (A)", title="Current"))
    time.sleep(1)
print("hello")