# Feature Spec: Question Answering System

**Status:** Implemented

## Summary
Answer user questions based on retrieved context from uploaded PDF documents using a local LLM.

## Motivation
Students need to ask questions about their study materials and receive accurate answers grounded in the uploaded content.

## Requirements
- Accept natural language questions via chat interface
- Retrieve relevant sections from processed PDF content
- Build context-aware prompts for the LLM
- Generate answers using TinyLlama via llama.cpp
- Display retrieved sources alongside answers
- Typewriter effect for natural reading experience
- Clear chat functionality

## API / Interface
- `manual_retrieval.py` — Embedding generation and similarity search
- `manual_llama.py` — LLM inference via llama.cpp
- `manual_qa.py` — End-to-end QA pipeline
- Streamlit chat UI

## Test Plan
- Manual testing with sample PDFs and questions
- Verify context restriction (no hallucination)

## Documentation Impact
- USER_MANUAL.md covers chat interaction
- README.md explains architecture
