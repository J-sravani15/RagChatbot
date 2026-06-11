# SKILLS.md

## StudentAI Capabilities

### PDF Processing

Description:

Extract text from uploaded PDF documents.

Tools:

* pypdf

Input:

* PDF files

Output:

* Raw text

---

## Text Chunking

Description:

Split large documents into smaller searchable chunks.

Current Configuration:

* Chunk Size: 3000
* Overlap: 300

Output:

* Text chunks

---

## Embedding Generation

Description:

Convert text chunks into vector representations.

Model:

all-MiniLM-L6-v2

Library:

sentence-transformers

Output:

* Embeddings

---

## Similarity Search

Description:

Find relevant chunks for a user query.

Method:

Cosine Similarity

Tools:

* NumPy

Output:

* Top matching chunks

---

## Retrieval-Augmented Generation (RAG)

Description:

Provide answers using retrieved document context.

Workflow:

Question
→ Embedding
→ Similarity Search
→ Retrieved Context
→ Llama3
→ Answer

---

## Conversational Interface

Description:

Maintain a chat-based interaction model.

Features:

* Chat history
* Context retrieval
* Follow-up questions

Framework:

Streamlit

---

## Typewriter Response

Description:

Display responses gradually for a better user experience.

Features:

* Word-by-word rendering
* Streaming-style output

---

## Thinking Indicator

Description:

Show progress while generating responses.

Features:

* Spinner animation
* Processing feedback

---

## PDF Knowledge Search

Description:

Search information from uploaded PDFs.

Supported:

* Academic Notes
* Books
* Lecture Slides (PDF)
* Research Papers

---

## Local AI Processing

Description:

Run all AI functionality locally.

Tools:

* Ollama
* Llama3

Benefits:

* No API costs
* No external dependencies
* Privacy-friendly

---

## Current Limitations

* No OCR
* No image understanding
* No handwritten note support
* No web search
* No citation tracking
* No embedding cache

---

## Planned Skills

### OCR Processing

* Scanned PDFs
* Handwritten notes

### Image Understanding

* JPG
* PNG
* JPEG

### Study Assistant Features

* Quiz Generation
* Flashcards
* Note Summarization
* Topic Extraction

### Advanced Retrieval

* Embedding Cache
* Metadata Search
* Source Citations
* Page References

### Deployment

* FastAPI Backend
* React Frontend
* Docker Support
* Cloud Deployment
