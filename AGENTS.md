# AGENTS.md

## Project Name

StudentAI

## Overview

StudentAI is a local Retrieval-Augmented Generation (RAG) chatbot designed for students to upload PDF study materials and ask questions based on the uploaded content.

The system runs completely locally using llama.cpp and does not require external APIs or vector databases.

---

## Primary Agent

### StudentAI Assistant

Role:

* Answer questions using uploaded PDF documents.
* Retrieve relevant context from processed PDF content.
* Generate accurate answers using llama.cpp TinyLlama.
* Refuse to hallucinate when information is not present in retrieved context.

Responsibilities:

1. Accept user questions.
2. Retrieve relevant chunks from uploaded PDFs.
3. Build context-aware prompts.
4. Generate answers from retrieved context.
5. Display retrieved sources.

---

## Retrieval Agent

Responsibilities:

* Generate embeddings from PDF chunks.
* Calculate cosine similarity.
* Select top matching chunks.
* Return context to the LLM.

Embedding Model:

all-MiniLM-L6-v2

---

## Document Processing Agent

Responsibilities:

* Extract text from PDFs.
* Clean extracted content.
* Create chunks.
* Prepare content for embedding generation.

Library:

pypdf

---

## LLM Agent

Responsibilities:

* Generate answers.
* Follow context restrictions.
* Avoid unsupported claims.

Model:

tinyllama-1.1b-chat-v1.0 (GGUF)

Provider:

llama.cpp

---

## UI Agent

Responsibilities:

* PDF upload interface.
* Chat interface.
* Typewriter effect.
* Thinking indicators.
* Display retrieved context.

Framework:

Streamlit

---

## Current Constraints

* PDF files only
* No image support
* No OCR support
* No database
* No internet search
* Local execution only

---

## Future Agents

### OCR Agent

Purpose:

* Extract text from scanned PDFs.

Possible Tools:

* Tesseract OCR
* EasyOCR

---

### Vision Agent

Purpose:

* Analyze images and diagrams.

Possible Models:

* LLaVA
* Qwen-VL

---

### Citation Agent

Purpose:

* Show page numbers and references for generated answers.

---

### Summarization Agent

Purpose:

* Summarize large PDFs.
* Generate study notes.
* Create revision guides.
