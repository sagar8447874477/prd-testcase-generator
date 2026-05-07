import streamlit as st
from model import generate_test_cases
from utils import read_pdf, read_text

# Page config
st.set_page_config(
    page_title="PRD to Test Cases Generator",
    page_icon="🧪",
    layout="centered"
)

# Title
st.title("🧪 PRD → QA Test Case Generator")

st.markdown("""
Upload a PRD document and automatically generate structured QA test cases.
""")

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "📄 Upload PRD File",
    type=["txt", "pdf"]
)

if uploaded_file:

    # Read file
    if uploaded_file.type == "application/pdf":
        prd_text = read_pdf(uploaded_file)
    else:
        prd_text = read_text(uploaded_file)

    # Show extracted text
    st.subheader("📄 Extracted PRD")

    st.text_area(
        "PRD Content",
        prd_text,
        height=250
    )

    # Generate button
    if st.button("🚀 Generate Test Cases"):

        with st.spinner("Generating test cases..."):

            output = generate_test_cases(prd_text)

        st.subheader("🧪 Generated Test Cases")

        st.text_area(
            "Output",
            output,
            height=500
        )

        # Download button
        st.download_button(
            label="📥 Download Test Cases",
            data=output,
            file_name="test_cases.txt",
            mime="text/plain"
        )