# FastAPI RAG API with Mistral‑7B & FAISS

A **production‑ready Retrieval‑Augmented Generation (RAG) API** built with **FastAPI**, **FAISS**, and **Mistral‑7B‑Instruct**. This project lets you query your own documents through an HTTP API while ensuring answers are grounded strictly in retrieved context.

> 🎯 **Goal:** Provide fast, accurate, and source‑aware answers from custom datasets with minimal hallucinations.

---

## 🚀 Key Features

- ⚡ **FastAPI** – High‑performance, async REST API
- 🧠 **Mistral‑7B‑Instruct** – Open‑weight LLM for generation
- 🔍 **FAISS Vector Store** – Fast similarity search at scale
- 🧩 **Retrieval‑Augmented Generation (RAG)** – Answers based only on retrieved context
- 📚 **Source Attribution** – Responses include supporting document chunks
- 🐳 **Docker & Docker Compose** – Easy local and server deployment
- 🔄 **Async‑Safe Inference** – Non‑blocking LLM execution
- 🔧 **Configurable Pipeline** – Chunking, embeddings, and model settings

---

## 🏗️ Architecture Overview

```
User Query
   ↓
FastAPI Endpoint
   ↓
Embedding Model
   ↓
FAISS Similarity Search
   ↓
Relevant Context Chunks
   ↓
RAG Prompt Assembly
   ↓
Mistral‑7B‑Instruct
   ↓
Answer + Sources
```

### How It Works

1. **Documents are ingested** and split into chunks
2. **Embeddings** are generated for each chunk
3. Chunks are stored in **FAISS** for fast retrieval
4. A user query is embedded and matched against FAISS
5. Top‑K relevant chunks are injected into a **RAG prompt**
6. **Mistral‑7B** generates an answer strictly from context
7. API returns the answer **with sources**

---

## 📁 Project Structure

```
.
├── app/                # FastAPI application logic
│   ├── api/            # API routes
│   ├── core/           # Configuration & settings
│   ├── rag/            # RAG pipeline (retrieval, prompts, generation)
│   └── models/         # Request/response schemas
├── data_storage/       # FAISS indexes and persisted data
├── docs/               # Additional documentation
├── frontend/           # (Optional) UI for querying the API
├── tests/              # Test suite
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📦 Installation

### Option 1: Docker (Recommended)

```bash
git clone https://github.com/DenysZakharovGH/FastAPI-RAG-API-with-Mistral-7B-FAISS.git
cd FastAPI-RAG-API-with-Mistral-7B-FAISS
docker-compose up --build
```

The API will be available at:
```
http://localhost:8000
```
---

[![Demo](docs/demo.gif)]

---

---

### Option 2: Local Setup

```bash
git clone https://github.com/DenysZakharovGH/FastAPI-RAG-API-with-Mistral-7B-FAISS.git
cd FastAPI-RAG-API-with-Mistral-7B-FAISS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🔌 API Usage

### Ask a Question

**Endpoint**
```
POST /ask
```

**Request Body**
```json
{
  "question": "What is the length of a giraffe's tongue?"
}
```

**Response**
```json
{
  "answer": "A giraffe's tongue typically measures between 18 and 20 inches in length.",
  "sources": [
    {
      "content": "Giraffe tongues can reach up to 20 inches...",
      "metadata": {
        "source": "animals.txt"
      }
    }
  ]
}
```

---

## 🧠 Hallucination Control

This project is designed to **minimize hallucinations**:

- The model is instructed to answer **only from provided context**
- If no relevant context is found, the model responds accordingly
- Prompt templates explicitly restrict speculative answers

---

## ⚙️ Configuration

Most settings can be configured via environment variables or config files:

- Embedding model
- Chunk size & overlap
- FAISS index type
- Number of retrieved chunks (Top‑K)
- LLM generation parameters (temperature, max tokens)

---

## 🧪 Testing

```bash
pytest
```

---

## 📈 Performance & Scaling Ideas

- GPU acceleration (FAISS‑GPU, CUDA‑enabled inference)
- Result caching (Redis)
- Streaming responses
- Multi‑index or multi‑tenant vector stores

---

## 🔐 Production Notes

- Add authentication (JWT / API keys)
- Enable request rate limiting
- Monitor latency and memory usage
- Use persistent volumes for FAISS indexes

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Denys Zakharov**  
GitHub: https://github.com/DenysZakharovGH

---
