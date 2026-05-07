import streamlit as st
from model import generate_test_cases
from utils import read_pdf, read_text

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="PRD → QA Test Generator",
    page_icon="🧪",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stApp {
    background: linear-gradient(to bottom right, #0E1117, #111827);
    color: white;
}

h1, h2, h3 {
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.feature-card {
    background-color: #111827;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #374151;
    text-align: center;
}

.stButton > button {
    width: 100%;
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

textarea {
    border-radius: 10px !important;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("""
# 🧪 PRD → QA Test Case Generator

Generate structured QA test plans automatically from Product Requirement Documents.

""")

st.markdown("---")

# ---------------- FEATURES SECTION ---------------- #
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📄 PRD Upload</h3>
        <p>Supports TXT and PDF documents</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🧠 AI-Assisted</h3>
        <p>Automatically generates QA test cases</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>✅ QA Coverage</h3>
        <p>Functional, Edge & Negative tests</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
with st.sidebar:

    st.title("⚙️ About")

    st.info("""
This application converts Product Requirement Documents into structured QA test cases.

### Features
- PRD Upload
- PDF/Text Support
- Functional Tests
- Edge Cases
- Negative Cases
- Download Output

### Tech Stack
- Python
- Streamlit
- NLP Heuristics
- Regex Parsing
""")

    st.markdown("---")

    st.subheader("🧪 Example PRD")

    st.code("""
Users should be able to login using email and password.

Forgot password should work using OTP.

The system should lock the account after 5 failed login attempts.
""")

# ---------------- MAIN CARD ---------------- #
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📤 Upload PRD")

uploaded_file = st.file_uploader(
    "Choose a PRD file",
    type=["txt", "pdf"]
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PROCESS FILE ---------------- #
if uploaded_file:

    with st.spinner("📄 Reading PRD..."):

        if uploaded_file.type == "application/pdf":
            prd_text = read_pdf(uploaded_file)
        else:
            prd_text = read_text(uploaded_file)

    # Extracted PRD Section
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📄 Extracted PRD Content")

    st.text_area(
        "",
        prd_text,
        height=250
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # Generate Button
    if st.button("🚀 Generate QA Test Cases"):

        with st.spinner("🧠 Generating structured test cases..."):

            output = generate_test_cases(prd_text)

        # Success Message
        st.success("✅ Test cases generated successfully!")

        # Output Card
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🧪 Generated QA Test Plan")

        st.text_area(
            "",
            output,
            height=600
        )

        st.markdown('</div>', unsafe_allow_html=True)

        # Download Button
        st.download_button(
            label="📥 Download Test Cases",
            data=output,
            file_name="generated_test_cases.txt",
            mime="text/plain"
        )

# ---------------- FOOTER ---------------- #
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; color:gray;'>
Built for AI QA Automation Assignment • Streamlit + Python
</div>
""", unsafe_allow_html=True)