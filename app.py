import uuid
import streamlit as st

from agents.severity_agent import severity_agent
from agents.root_cause_agent import root_cause_agent
from agents.fix_agent import fix_agent
from agents.prevention_agent import prevention_agent
from agents.report_agent import report_agent


st.set_page_config(
    page_title="AI DevOps Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI DevOps Copilot")
st.subheader("AI-Powered CI/CD Failure Investigator")


uploaded_file = st.file_uploader(
    "Upload CI/CD Log",
    type=["txt", "log"]
)


if uploaded_file:

    log_text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Log")

    st.code(
        log_text,
        language="text"
    )

    if st.button("🚀 Investigate Incident"):

        with st.spinner("Running AI Agents..."):

            severity = severity_agent(log_text)

            root_cause = root_cause_agent(log_text)

            fix = fix_agent(log_text)

            prevention = prevention_agent(
                log_text,
                root_cause
            )

            report = report_agent(
                severity,
                root_cause,
                fix,
                prevention
            )

        incident_id = str(uuid.uuid4())[:8]

        st.success(
            f"Incident ID: {incident_id}"
        )

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "🚨 Severity",
                "🔍 Root Cause",
                "🛠 Fix",
                "🛡 Prevention",
                "📄 Report"
            ]
        )

        with tab1:
            st.markdown(severity)

        with tab2:
            st.markdown(root_cause)

        with tab3:
            st.markdown(fix)

        with tab4:
            st.markdown(prevention)

        with tab5:
            st.markdown(report)

            st.download_button(
                "📥 Download Incident Report",
                report,
                f"incident_{incident_id}.txt",
                "text/plain"
            )

else:

    st.info(
        "Upload a CI/CD log file to begin investigation."
    )