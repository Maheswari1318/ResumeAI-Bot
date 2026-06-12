# 🤖 Resume AI Chatbot

An AI-powered Resume Chatbot built using Python, Streamlit, Ollama, and Qwen. The chatbot reads resume information from a PDF file and answers user questions based on the resume content.

## 🚀 Features

* Resume-based Question Answering
* PDF Text Extraction using PyPDF2
* Local LLM Inference using Ollama
* Qwen 2.5 Language Model
* Streamlit Web Interface
* GitHub and LinkedIn Integration
* Education, Skills, Projects, and Internship Information
* No API Cost (Runs Locally)

## 🛠️ Technologies Used

* Python
* Streamlit
* PyPDF2
* Ollama
* Qwen 2.5:3B
* VS Code

## 📂 Project Structure

ResumeChatBot/

├── app.py

├── resume.pdf

├── requirements.txt

└── README.md

## ⚙️ Installation

### Clone Repository


git clone <repository-url>
cd ResumeChatBot


### Create Virtual Environment


python -m venv venv

### Activate Environment


venv\Scripts\activate


### Install Dependencies


pip install -r requirements.txt


## 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com

Verify installation:


ollama --version


## 📥 Download Llama Model


ollama pull Llama 3.2


## ▶️ Run Application


python -m streamlit run app.py


The application will be available at:

http://localhost:8501

# 💬 Example Questions

* Tell me about yourself
* What are your technical skills?
* What projects have you worked on?
* Tell me about your internship experience
* What is your educational background?
* What is your GitHub profile?
* What is your LinkedIn profile?

# 🔮 Future Enhancements

* RAG (Retrieval-Augmented Generation)
* ChromaDB Integration
* Multi-Resume Support
* Groq API Deployment
* Voice-Based Interaction

# 👩‍💻 Author

Uma Maheswari

GitHub:
https://github.com/Maheswari1318

LinkedIn:
https://www.linkedin.com/in/umamaheswari1318
