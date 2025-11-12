import streamlit as st

st.title("Channel Settings")

channels = ["Channel 1", "Channel 2"]
defaults = {"Imax": 1.0, "Vmax": 3.0, "Pmax": 20.0, "Vmin": 0.5}

for ch in channels:
    with st.expander(ch):
        st.number_input(f"{ch} - Imax (A)", value=defaults["Imax"], step=0.1)
        st.number_input(f"{ch} - Vmax (V)", value=defaults["Vmax"], step=0.1)
        st.number_input(f"{ch} - Pmax (W)", value=defaults["Pmax"], step=0.5)
        st.number_input(f"{ch} - Vmin (V)", value=defaults["Vmin"], step=0.1)
        st.toggle(f"{ch} - Power", value=False)
