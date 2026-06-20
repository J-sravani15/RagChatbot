# Feature Spec: PDF Processing

**Status:** Implemented

## Summary
Extract and clean text content from uploaded PDF files for downstream RAG processing.

## Motivation
Users need to upload PDF study materials and have the system extract text to enable question answering.

## Requirements
- Accept PDF file uploads via Streamlit UI
- Extract text content using PyMuPDF4LLM
- Clean extracted text (remove headers/footers, normalize whitespace)
- Split content into logical sections for retrieval
- Handle multiple PDF uploads in a single session

## API / Interface
- `manual_extract.py` — CLI-based PDF text extraction
- `manual_sections.py` — Section splitting and chunking
- Streamlit file uploader widget for UI-based uploads

## Test Plan
- Unit tests for section building in `tests/test_sections.py`
- Manual verification with sample PDFs

## Documentation Impact
- USER_MANUAL.md documents upload workflow
- README.md covers architecture
