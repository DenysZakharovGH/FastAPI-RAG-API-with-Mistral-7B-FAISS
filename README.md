# 🚀 FastAPI RAG API with Mistral-7B & FAISS

A **production-ready Retrieval-Augmented Generation (RAG) API** built with **FastAPI**, **FAISS**, and **Mistral-7B-Instruct**.

This project demonstrates how to build a **controlled, async-safe LLM backend** that answers questions **only from your own data**, minimizing hallucinations while keeping latency and costs under control.

---

## ✨ Features

* ⚡ **FastAPI (ASGI)** — high-performance async web framework
* 🧠 **Mistral-7B-Instruct** — powerful open-weight LLM
* 🔍 **FAISS Vector Database** — fast cosine similarity search
* 🧩 **Complete RAG pipeline**

  * ingestion
  * chunking
  * embeddings
  * retrieval
  * generation
* 🧵 **Async-safe LLM execution** using `run_in_threadpool`
* 📦 **Metadata support** (source, document info per chunk)
* 🛡️ **Hallucination control** (answers only from retrieved context)
* 📏 **Token-aware prompt construction**
* 🔄 **Background tasks** for logging
* 🐳 **Docker-ready architecture**

---

## 🏗️ Architecture

```
Client
  ↓
FastAPI (async)
  ↓
Pydantic Validation
  ↓
FAISS Similarity Search
  ↓
RAG Prompt Assembly
  ↓
Mistral-7B-Instruct
  ↓
Answer + Sources
```

---

## 🔧 Requirements

* Python **3.10+**
* GPU recommended (**≥ 8GB VRAM**)
* Linux / Windows / macOS

### Python dependencies

```bash
pip install -r requirements.txt
```

Main libraries:

* `fastapi`
* `uvicorn`
* `torch`
* `transformers`
* `faiss-cpu` or `faiss-gpu`
* `sentence-transformers`

---

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
```

Open API docs:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📤 Example Request

```http
POST /ask
Content-Type: application/json

{
  "question": "Length of a giraffe tongue?"
}
```

### 📥 Example Response

```json
{
  "answer": "The length of a giraffe's tongue can measure between 18 to 20 inches.",
  "sources": [
    "The giraffes tongue is about 18 inches long",
    "giraffes have a 17 inch long tongue",
    "A giraffes tongue can measure 20 inches in length"
  ]
}
```
---

[![Demo](docs/demo.gif)]

---

## 🧠 RAG Pipeline Explained

### 1️⃣ Ingestion

Load raw documents and store their source information.

### 2️⃣ Chunking

Split documents into **300–500 token chunks** with overlap.

### 3️⃣ Embeddings

Convert text chunks into vectors using a sentence embedding model.

### 4️⃣ Vector Database

Store embeddings in **FAISS** for fast similarity search.

### 5️⃣ Retrieval

Search for **top-k most similar chunks** using cosine similarity.

### 6️⃣ Prompt Assembly

Inject retrieved context into an instruction-based prompt.

### 7️⃣ Generation

Generate an answer using **Mistral-7B-Instruct**.

---

## 🛡️ Hallucination Control

The model is explicitly instructed:

> *If the answer is not in the provided context, say "I don't know".*

Additional safety:

* limited context window
* source-aware responses
* optional similarity confidence threshold

---

## 🧵 Async-Safe LLM Execution

LLM inference is **blocking**, so it is executed safely using:

```python
await run_in_threadpool(generate_answer, prompt)
```

This prevents blocking the FastAPI event loop and allows concurrent requests.

---

## 🐳 Docker (Optional)

```bash
docker build -t rag-api .
docker run -p 8000:8000 rag-api
```

Docker Compose support can be added for:

* GPU
* Redis cache
* external vector stores

---

## 📌 Use Cases

* Internal knowledge assistants
* Document Q&A systems
* RAG-powered chatbots
* AI search APIs
* LLM experimentation with full data control

---

## 🔮 Roadmap

* ⚡ Streaming responses (token-by-token)
* 🧵 Concurrency limiter (Semaphore)
* 🛡️ Hallucination confidence scoring
* 💾 Redis caching
* 🐳 GPU-optimized Docker Compose

---

## 🧠 Philosophy

> **LLMs should answer only what your data allows them to answer.**

This project focuses on **correctness, observability, and control** rather than raw generation.

---

## 📄 License

MIT License

