# StudentAI Local Document Q&A

## Goal

Implement a local-first document question-answering workflow using PyMuPDF4LLM and llama.cpp.

## Requirements

* Upload one or more PDF documents.
* Extract document content using PyMuPDF4LLM.
* Split content into structured sections.
* Retrieve relevant sections based on user questions.
* Generate answers using llama.cpp.
* Display retrieved context.

## Acceptance Criteria

* User can upload PDFs.
* PDFs are processed successfully.
* Questions return relevant answers.
* Retrieved context is visible.
* Application runs locally.

## Test Plan

* Verify PDF upload.
* Verify section extraction.
* Verify retrieval quality.
* Verify answer generation.
