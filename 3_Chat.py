import streamlit as st
import ollama
import json
from pathlib import Path

# --- CONFIG ---
DATA_DIR = Path("/Users/ibrahimfourati/PycharmProjects/Embedded/data")
TELEMETRY_PATH = DATA_DIR / "telemetry.json"
HISTORY_PATH = DATA_DIR / "chat_history.json"
MAX_HISTORY = 10

st.set_page_config(page_title="PromptWATT AI Assistant ⚡", page_icon="⚡")
st.title("PromptWATT AI Assistant ⚡")
st.markdown("Ask questions about power usage, channel status, or get AI-based insights.")

# --- UTILS ---
def save_json(path: Path, data):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        st.error(f"⚠️ Error saving {path.name}: {e}")

def load_telemetry():
    return load_json(TELEMETRY_PATH, default={})

def load_json(path: Path, default=None):
    if path.exists():
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return data
        except Exception as e:
            st.warning(f"⚠️ Could not read {path.name}: {e}")
    return default


def load_history():
    data = load_json(HISTORY_PATH, default=[])
    # Ensure we always have a list (avoid slice errors)
    if not isinstance(data, list):
        st.warning(f"⚠️ Invalid chat history format in {HISTORY_PATH.name}. Resetting it.")
        data = []
    return data[-MAX_HISTORY:]


def save_history(messages):
    # Keep only the last MAX_HISTORY messages
    if not isinstance(messages, list):
        messages = []
    save_json(HISTORY_PATH, messages[-MAX_HISTORY:])


# --- LOAD TELEMETRY ---
telemetry_data = load_telemetry()
if telemetry_data:
    st.success("✅ Telemetry data loaded.")
else:
    st.warning("⚠️ No telemetry found yet.")
st.json(telemetry_data)

# --- LOAD / INIT CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = load_history()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- USER INPUT ---
if prompt := st.chat_input("Ask me about your system..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    context = json.dumps(telemetry_data, indent=2)
    system_prompt = (
        "You are PromptWATT, an AI assistant analyzing real power monitoring telemetry.\n"
        "Use this data to answer clearly and give recommendations:\n"
        f"{context}"
    )

    # --- OLLAMA CALL ---
    with st.chat_message("assistant"):
        with st.spinner("Analyzing telemetry..."):
            response = ollama.chat(
                model="llama3.2:1b",
                messages=[{"role": "system", "content": system_prompt}]
                         + st.session_state.messages
            )
            reply = response["message"]["content"]
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    save_history(st.session_state.messages)
