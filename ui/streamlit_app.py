import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")

# 🔥 SIDEBAR (HISTORY)
st.sidebar.title("📚 History")

try:
    history = requests.get(f"{API}/history").json()

    if len(history) == 0:
        st.sidebar.write("No history yet")
    else:
        for i, item in enumerate(history[:10]):
            with st.sidebar.expander(f"Error {i+1}"):
                st.write("🧾 Error:")
                st.write(item["error"])

                st.write("🛠 Fix:")
                st.write(item["fix"][:200] + "...")

except:
    st.sidebar.error("Backend not running")

# 🔥 MAIN UI
st.title("🛠 Self-Healing API Agent")

log = st.text_area("Paste Error Log")

if st.button("Analyze & Fix"):

    if not log:
        st.warning("Enter error log")
    else:
        try:
            res = requests.post(f"{API}/heal", json={"log": log}, timeout=60)
            res = res.json()

            st.subheader("🔍 Analysis")
            st.write(res["analysis"])

            st.subheader("🛠 Fix Suggestion")
            st.code(res["fix"])

            st.subheader("📊 Confidence")
            st.metric("Score", res["confidence"])

        except requests.exceptions.ConnectionError:
            st.error("🚨 Backend not running")

        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out")