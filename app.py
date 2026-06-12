import streamlit as st
from PyPDF2 import PdfReader
import ollama

reader = PdfReader("resume.pdf")

resume_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text

st.set_page_config(
    page_title="Resume AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Resume AI Chatbot")
st.write("Ask anything about my resume.")

st.sidebar.title("Connect")

st.sidebar.markdown(
    "[GitHub](https://github.com/Maheswari1318)"
)

st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/in/umamaheswari1318)"
)

question = st.text_input("Ask anything about me")

if question:

    q = question.lower()

    if "skill" in q or "technology" in q:

        st.markdown("""
### 💻 SKILLS

#### Programming Languages
- Python
- Java (Basics)

#### Web Technologies
- HTML
- CSS
- JavaScript
- React (Basics)

#### Database
- MySQL

#### Tools
- GitHub
- VS Code
- Jupyter Notebook
- Eclipse

#### Concepts
- OOPs
- REST APIs
- Generative AI
""")

    elif "project" in q:

        st.markdown("""
### 🚀 PROJECTS

#### 1. Gen AI Chatbot LLMs
- Developed a chatbot with text and image input.
- Built using Python, HTML, CSS, and JavaScript.
- Leveraged Large Language Models (LLMs) for automated support.

#### 2. Weather Analysis Application
- Developed a weather analysis web application using React.js.
- Integrated REST APIs to fetch live weather data.

#### 3. Habit-Aware Finance
- Built a full-stack finance tracking application.
- Tech Stack: Python, Flask, SQLite/JSON, HTML/CSS.
""")

    elif "intern" in q or "internship" in q:

        st.markdown("""
### 💼 INTERNSHIPS

#### AI Intern – Techobytes, E-Cell
(May–June 2024)

- Voice Cloning (RVC)
- Object Detection (YOLO)
- Generative AI Chatbots
- Integrated AI models into production systems

#### Application Developer – Rooman Technologies
(Feb–May 2025)

- Web and Mobile Application Development
- UI Integration
- API Integration
- Debugging and Optimization
""")

    elif "github" in q:

        st.markdown(
            "[🔗 GitHub Profile](https://github.com/Maheswari1318)"
        )

    elif "linkedin" in q:

        st.markdown(
            "[🔗 LinkedIn Profile](https://www.linkedin.com/in/umamaheswari1318)"
        )

    elif "about" in q or "yourself" in q or "introduce" in q:

        st.markdown("""
### 👋 About Me

I am Uma Maheswari, passionate about AI, Web Development, and Software Development.

My interests include:
- Generative AI
- Machine Learning
- Full Stack Development
- Building AI-powered applications
""")

    else:

        prompt = f"""
You are a professional AI assistant representing Uma Maheswari.

Rules:
1. Answer ONLY using information present in the resume.
2. Do NOT invent information.
3. If the answer is not available in the resume, reply:
   "I don't have that information in my resume."

Resume:
{resume_text}

Question:
{question}
"""

        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.write(response["message"]["content"])

        except Exception as e:
            st.error(f"Error: {e}")