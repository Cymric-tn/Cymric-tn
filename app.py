import streamlit as st

st.set_page_config(
    page_title="PromptWATT",
    page_icon="⚡",
    layout="wide",
)

st.sidebar.title("PromptWATT")
st.sidebar.write("Navigation:")
st.sidebar.page_link("pages/1_Graphs.py", label="Graphs")
st.sidebar.page_link("pages/2_Settings.py", label="Settings")
st.sidebar.page_link("pages/3_Chat.py", label="Chat")

st.title("PromptWATT Dashboard")
st.markdown("""
Welcome to **PromptWATT**, an AI-assisted power monitoring dashboard.

Use the sidebar to navigate:
- **Graphs**: View live voltage, current, and power.
- **Settings**: Configure channel limits.
- **Chat**: Ask the AI assistant questions about system performance.
""")
