import streamlit as st

from agents.analyzer import analyze_log
from agents.root_cause import root_cause
from agents.fix_generator import generate_fix
from agents.severity_agent import classify_severity

from utils.storage import (
    save_incident,
    load_incidents
)

st.set_page_config(
    page_title="AI DevOps Copilot",
    layout="wide"
)

st.title("🤖 AI DevOps Copilot")

# -----------------------
# Dashboard Section
# -----------------------

incidents = load_incidents()

total = len(incidents)

critical = sum(
    1 for i in incidents
    if "critical" in i["severity"].lower()
)

high = sum(
    1 for i in incidents
    if "high" in i["severity"].lower()
)

medium = sum(
    1 for i in incidents
    if "medium" in i["severity"].lower()
)

low = sum(
    1 for i in incidents
    if "low" in i["severity"].lower()
)

st.subheader("📊 Incident Dashboard")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total", total)
c2.metric("Critical", critical)
c3.metric("High", high)
c4.metric("Medium", medium)
c5.metric("Low", low)

st.divider()

# -----------------------
# Upload Section
# -----------------------

uploaded_file = st.file_uploader(
    "Upload CI/CD Log",
    type=["txt", "log"]
)

if uploaded_file:

    log_text = uploaded_file.read().decode()

    st.subheader("Uploaded Log")

    st.text_area(
        "Log Content",
        log_text,
        height=250
    )

    if st.button("Analyze"):

        with st.spinner("Running AI Agents..."):

            summary = analyze_log(log_text)

            severity = classify_severity(log_text)

            cause = root_cause(log_text)

            fix = generate_fix(log_text)

            incident = {
                "severity": severity,
                "summary": summary,
                "cause": cause
            }

            save_incident(incident)

        st.success("Analysis Complete")

        st.subheader("🚨 Severity")
        st.write(severity)

        st.subheader("📋 Analysis")
        st.write(summary)

        st.subheader("🔍 Root Cause")
        st.write(cause)

        st.subheader("🛠 Suggested Fix")
        st.write(fix)

# -----------------------
# Incident History
# -----------------------

st.divider()

st.subheader("📚 Incident History")

if incidents:

    for idx, incident in enumerate(
        reversed(incidents),
        start=1
    ):

        with st.expander(
            f"Incident {idx}"
        ):

            st.write(
                f"Severity: {incident['severity']}"
            )

            st.write(
                f"Summary: {incident['summary']}"
            )

            st.write(
                f"Cause: {incident['cause']}"
            )

else:

    st.info(
        "No incidents recorded yet."
    )