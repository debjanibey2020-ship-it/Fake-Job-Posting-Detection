import streamlit as st

st.set_page_config(page_title="Fake Job Detection", layout="centered")

st.title("🕵️ Fake Job Posting Detection")
st.write("Paste a job description to check whether it is REAL or FAKE.")

job_text = st.text_area("Paste Job Description Here", height=180)

def detect_fake_job(text):
    text = text.lower()

    strong_scam_patterns = [
        "processing fee",
        "registration fee",
        "send money",
        "pay ₹",
        "pay rs",
        "selected without interview",
        "no interview",
        "whatsapp only",
        "telegram only",
        "urgent hiring no interview"
    ]

    for pattern in strong_scam_patterns:
        if pattern in text:
            return "FAKE"

    return "REAL"

if st.button("Check Job"):
    if job_text.strip() == "":
        st.warning("Please enter job description.")
    else:
        result = detect_fake_job(job_text)

        if result == "FAKE":
            st.error("🚨 This job posting is FAKE")
            st.info("Reason: Scam-related patterns detected.")
        else:
            st.success("✅ This job posting is REAL")
            st.info("No scam patterns detected.")
