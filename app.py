import streamlit as st

from agents.analyzer import analyze_log
from agents.root_cause import root_cause
from agents.fix_generator import generate_fix

st.set_page_config(page_title="AI CI/CD Agent")

st.title("🤖 AI CI/CD Failure Analyzer")

uploaded_file = st.file_uploader(
    "Upload CI/CD Log",
    type=["txt", "log"]
)

if uploaded_file:

    log_text = uploaded_file.read().decode()

    st.code(log_text[:3000])

    if st.button("Analyze"):

        with st.spinner("Running AI Agents..."):

            summary = analyze_log(log_text)
            cause = root_cause(log_text)
            fix = generate_fix(log_text)

        st.subheader("Analysis")
        st.write(summary)

        st.subheader("Root Cause")
        st.write(cause)

        st.subheader("Suggested Fix")
        st.write(fix)