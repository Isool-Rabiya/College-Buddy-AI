import os
import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash')

st.title("College Buddy - AI Student Support")
st.write("Notes upload pannu, doubt kelu da!")

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

uploaded = st.file_uploader("Notes PDF upload pannu", type="pdf")
if uploaded:
    reader = PdfReader(uploaded)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    st.session_state.pdf_text = text
    st.success("PDF add aayiduchu da!")

question = st.text_input("Enna doubt? Kekalam da!")

if st.button("Kelu"):
    if question and st.session_state.pdf_text:
        prompt = f"Notes: {st.session_state.pdf_text[:10000]}\nQuestion: {question}\nAnswer in simple Tamil+English mix."
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("First PDF upload pannu aprom question kelu da!")