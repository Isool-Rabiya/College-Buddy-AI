import streamlit as st

st.set_page_config(
    page_title="AI Student Support Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("""
<style>
.main-title {
    background: linear-gradient(90deg, #2563eb, #1e40af);
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.main-title h1 {
    margin: 0;
    font-size: 30px;
}

.main-title p {
    margin: 8px 0 0 0;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:

    st.header("⚙️ Control Panel")

    st.subheader("📚 Study Material")

    uploaded_file = st.file_uploader(
        "Upload your college PDF",
        type=["pdf"]
    )

    st.divider()

    st.subheader("🤖 Assistant Mode")

    mode = st.selectbox(
        "Choose Mode",
        [
            "Student Support",
            "Exam Preparation",
            "College FAQ"
        ]
    )

    st.divider()

    st.write("### 🕒 Status")

    if uploaded_file:
        st.success("PDF Uploaded")
        st.write(uploaded_file.name)
    else:
        st.info("No PDF uploaded")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

# ---------- HEADER ----------
st.markdown("""
<div class="main-title">
    <h1>🎓 AI Student Support Assistant</h1>
    <p>AI-Powered Student Support Agent • College FAQ • Syllabus • Regulations • Notices</p>
</div>
""", unsafe_allow_html=True)

# ---------- COLUMNS ----------
chat_col, capability_col = st.columns([3, 1])

# ---------- CHAT ----------
with chat_col:

    st.subheader("💬 Chat")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        if message["role"] == "user":
            st.chat_message("user").write(message["content"])

        else:
            st.chat_message("assistant").write(message["content"])

    question = st.chat_input(
        "Ask your question..."
    )

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        st.chat_message("user").write(question)

        # Temporary response
        answer = f"""
I received your question:

**{question}**

📚 Please upload your college study material.  
I will use the uploaded documents to provide an accurate answer.
"""

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.chat_message("assistant").write(answer)

# ---------- CAPABILITIES ----------
with capability_col:

    st.subheader("✨ Capabilities")

    st.info("""
    📚 **College Documents**

    Answers questions from uploaded college materials.
    """)

    st.info("""
    📖 **Syllabus Support**

    Helps students understand subjects and syllabus.
    """)

    st.info("""
    📋 **College Regulations**

    Answers questions about college rules.
    """)

    st.info("""
    🔔 **Notices & FAQs**

    Finds information from college notices and FAQs.
    """)

    st.info("""
    🎯 **Exam Support**

    Helps students prepare for exams.
    """)