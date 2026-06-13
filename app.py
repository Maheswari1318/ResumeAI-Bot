import streamlit as st
from PyPDF2 import PdfReader
import ollama


# Streamlit Page Config

st.set_page_config(
    page_title="Resume AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Read Resume PDF

try:
    reader = PdfReader("resume.pdf")

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

except Exception as e:
    st.error(f"Error loading resume: {e}")
    st.stop()


# Title

st.title("🤖 Resume AI Chatbot")


# Sidebar

st.sidebar.title("🔗 Connect")

st.sidebar.markdown(
    "[GitHub](https://github.com/Maheswari1318)"
)

st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/in/umamaheswari1318)"
)

# User Input

question = st.text_input(
    "Ask anything about my resume"
)

# Chatbot Logic

if question:

    prompt = f"""
You are Uma Maheswari's Resume AI Assistant.

STRICT RULES:

1. Answer ONLY using information available in the resume.
2. Do NOT use outside knowledge.
3. Do NOT make assumptions.
4. Do NOT generate information that is not present in the resume.
5. Do NOT mix projects, internships, skills, education, or certifications.
6. If the answer is not available in the resume, reply EXACTLY:

Sorry, I can only answer questions based on the resume.

7. Keep answers concise and professional.

Resume:
{resume_text}

Question:
{question}
"""

    try:

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are a Resume AI Assistant.

Answer ONLY from the resume content provided.
Never use outside knowledge.
If information is missing, reply:
Sorry, I can only answer questions based on the resume.
"""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Answer")
        st.write(response["message"]["content"])

    except Exception as e:
        st.error(f"Error: {e}")

