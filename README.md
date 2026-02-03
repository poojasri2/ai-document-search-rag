# AI Document Search (RAG-based Question Answering System)

## 📌 Project Overview
This project is an AI-powered document question-answering system built using the
Retrieval-Augmented Generation (RAG) approach.

The system allows users to ask questions and receive answers based only on the
content of provided PDF documents, making the responses more accurate and reliable.

---

## 🎯 Problem Statement
Traditional AI chatbots often generate generic or incorrect answers.
This project solves that issue by grounding answers in actual document content
using semantic search and retrieval techniques.

---

## 🧠 How the System Works (Simple Explanation)
1. PDF documents are loaded from the `data/` folder
2. Documents are split into smaller text chunks
3. Each chunk is converted into vector embeddings
4. FAISS retrieves the most relevant chunks
5. A language model generates answers using retrieved content only
6. The final answer is returned through an API response

---

## 🛠️ Technologies Used
- Python
- FastAPI
- LangChain
- FAISS
- OpenAI API
- Swagger UI

---

## 📂 Project Structure
RAG-with-Langchain-and-FastAPI/
│
├── main.py            # FastAPI application entry point
├── endpoints.py       # API endpoints with error handling
├── qa_engine.py       # RAG logic (retrieval + generation)
├── data/              # PDF documents used for querying
├── requirements.txt   # Project dependencies
└── README.md
---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
git clone https://github.com/poojasri2/ai-document-search-rag.git
cd ai-document-search-rag

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Add PDF Documents
Place your PDF files inside the data/ folder.

### 4️⃣ Run the Application
python -m uvicorn main:app --reload

### 5️⃣ Open Swagger UI
http://127.0.0.1:8000/docs
---

## 📌 Output
The system exposes a REST API using FastAPI.
Users can query the system through Swagger UI and receive answers
based on the content of PDF documents.

### Sample Response
{
  "query": "What is machine learning?",
  "response": "Machine learning is a subset of artificial intelligence that enables systems to learn from data."
}
---

## ⚠️ Error Handling
- Handles missing or invalid queries gracefully
- Prevents server crashes using exception handling
- Returns meaningful HTTP error responses
- Improves robustness and reliability of the system
---

## 👨‍🎓 Academic Relevance
This project demonstrates key Computer Science concepts including:
- Artificial Intelligence
- Information Retrieval
- Backend Development
- REST API Design
- Software Engineering best practices
