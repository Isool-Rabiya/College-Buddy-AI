import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import os

# TODO: Itha un API key ah maathu da - aistudio.google.com la free ah kedaikkum
genai.configure(api_key="PASTE_YOUR_GEMINI_KEY_HERE")

st.set_page_config(page_title="Student Support Agent")
st.title("🎓 AI Student Support Assistant")

st.write("College rules, syllabus pathi etha kettalum solluven da!")

# PDF padikkira function
def get_pdf_text():
    # oru sample text - PDF illa na kooda work aagum
    return """
    College Regulations:
    - Attendance 75% must
    - ID Card compulsory
    - Exam: 2 Internal + 1 Model + Final
    - Leave: Need HOD permission
    - Library: 9AM to 5PM
    """

pdf_data = get_pdf_text()

# Chat history memory
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User kekura question
if question := st.chat_input("Enna doubt da?"):
    st.session_state.messages.append({"role":"user", "content": question})
    st.chat_message("user").write(question)

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"College Data: {pdf_data}\n\nStudent Question: {question}\nAnswer in simple Tamil+English:"
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"API Key poda maranthuta da! Error: {e}"

    st.session_state.messages.append({"role":"assistant", "content": answer})
    st.chat_message("assistant").write(answer)