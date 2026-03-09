# AI Agent Assistant

A modular AI agent capable of answering questions using multiple tools including **document retrieval, web search, and mathematical reasoning**.
Users can upload PDF documents and ask questions based on their content.

This project demonstrates a **Retrieval Augmented Generation (RAG) pipeline combined with tool-based AI agent reasoning**.

---

# Features

* 📄 PDF document question answering (RAG)
* 🌐 Web search for general knowledge queries
* ➗ Mathematical calculation tool
* 🖥 Streamlit chat interface
* ⚡ FastAPI backend
* 🧠 Vector database for document retrieval
* 📊 Logging for agent tool usage

---

# System Architecture

```
User
 │
 ▼
Streamlit UI
 │
 ▼
FastAPI Backend
 │
 ▼
Agent Controller
 │
 ├── Vector Search Tool (RAG)
 │      └── PDF → Chunking → Embeddings → Vector DB
 │
 ├── Web Search Tool
 │
 └── Math Tool
```

---

# Agent Workflow

## 1. PDF Upload Workflow

The user uploads a PDF through the Streamlit interface.

Processing pipeline:

```
PDF Upload
   ↓
Document Loader
   ↓
Text Chunking
   ↓
Embedding Generation
   ↓
Vector Database Storage
```

### Steps

1. User uploads a PDF file in the UI
2. File is saved in the **data/** directory
3. FastAPI endpoint `/upload_pdf` receives the file path
4. The document loader reads the PDF
5. Text is split into chunks
6. Each chunk is converted into embeddings
7. Embeddings are stored in the vector database

---

# Question Answering Workflow

When a user asks a question:

```
User Question
      ↓
FastAPI /ask endpoint
      ↓
Agent Controller
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
Response Returned to User
```

The agent analyzes the question and selects the appropriate tool.

---

# Tool Selection Logic

| Query Type                         | Tool Used     |
| ---------------------------------- | ------------- |
| Questions about uploaded documents | Vector Search |
| General knowledge questions        | Web Search    |
| Mathematical expressions           | Math Tool     |

---

# Project Structure

```
ai_agent
│
├── app
│   ├── main.py
│   ├── routes.py
│   ├── agent_controller.py
│   │
│   └── rag
│       ├── document_loader.py
│       ├── chunking.py
│       └── vector_store.py
│
├── ui
│   └── streamlit_app.py
│
├── data
│   └── uploaded_pdfs
│
└── README.md
```

---

# Installation

## 1. Clone the repository

```
git clone <repository-url>
cd ai_agent
```

---

## 2. Create a virtual environment

```
python -m venv venv
```

Activate the environment.

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

## Start the Backend Server

Run the FastAPI server:

```
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Start the Streamlit UI

Run the Streamlit application:

```
streamlit run ui/streamlit_app.py
```

The UI will open at:

```
http://localhost:8501
```

---

# Working Demo

## Step 1 – Upload PDF

Upload a PDF through the Streamlit interface.

Example:

```
LLM Guide.pdf
```

After clicking **Process PDF**, the backend processes the document.

Example logs:

```
File path received: data/llm.pdf
Docs loaded: 12
Chunks created: 48
Documents stored in vector DB
```

---

## Step 2 – Ask Questions

Example queries:

```
What is an LLM?
Explain tokenization.
What are tokens in language models?
```

The agent retrieves relevant chunks from the vector database and generates an answer.

---

# Example Agent Interaction

```
User: What is an LLM?

Agent: LLM stands for Large Language Model. It is a deep learning model trained on massive text datasets to understand and generate human language.
```

---

# Logs of Tool Usage

The system logs agent actions using the logging system.

---

## Example 1 – Vector Search Tool

User query:

```
what is llm from the uploaded document?
```

Logs:

```
INFO | Received question: what is llm from the uploaded document?
INFO | Agent received query
INFO | Using vector search tool
INFO | Knowledge base search called
INFO | Searching for relevant chunks
INFO | Generating embedding
```

Explanation:
The agent recognized that the query relates to the uploaded document and used the **vector retrieval tool**.

---

## Example 2 – Web Search Tool

User query:

```
what is a token?
```

Logs:

```
INFO | Received question: what is a token?
INFO | Agent received query
INFO | Using web search tool
INFO | Web search tool called
```

Explanation:
Since the question is general knowledge, the agent used the **web search tool**.

---

## Example 3 – Math Tool

User query:

```
calculate 25 * 14
```

Logs:

```
INFO | Received question: calculate 25 * 14
INFO | Agent received query
INFO | Using math tool
INFO | Executing calculation
```

---

# Technologies Used

| Component       | Technology                     |
| --------------- | ------------------------------ |
| Backend API     | FastAPI                        |
| UI              | Streamlit                      |
| Vector Database | ChromaDB                       |
| Embeddings      | OpenAI / Sentence Transformers |
| Logging         | Loguru                         |
| Language        | Python                         |

---

# Key Concepts Demonstrated

* Retrieval Augmented Generation (RAG)
* Tool-based AI agents
* Document question answering
* Vector similarity search
* Conversational AI
* API-based AI architecture

---

# Future Improvements

Potential enhancements:

* Conversation memory using advanced memory modules
* Multi-document support
* Source citation for answers
* Streaming responses
* Authentication system
* Docker deployment
* Cloud deployment

---

# Summary

This project demonstrates how to build a **multi-tool AI agent system** that can:

* Answer questions from uploaded documents
* Search the web for general information
* Perform mathematical reasoning
* Log tool usage for transparency

It showcases practical concepts used in modern AI systems such as **RAG, vector databases, and tool-based reasoning agents**.

